from hashlib import new
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse, HttpResponse
from rest_framework import status

from api.models import Books, Library, LibraryBooks
from api.serializers import BooksSerializer, LibrarySerializer, LibraryBooksSerializer
from api.messages import *


from django.db import connection
import api.queries as q
import json


@csrf_exempt
def libraries(request):
    if request.method == "GET":
        try:
            data = JSONParser().parse(request)
            page = None
            size = None
            city = None
            if 'size' in data:
                size = data['size']
            if 'page' in data:
                page = data['page']
            if page is not None and size is not None:
                pass # ???

            if 'city' in data:
                city = data['city']
                try:
                    libraries =  Library.objects.filter(city=city).all()
                    library_serializer =  LibrarySerializer(libraries, many=True)
                    return JsonResponse(library_serializer.data, safe=False, status=status.HTTP_200_OK)
                except Exception:
                    return HttpResponse(status=status.HTTP_404_NOT_FOUND)
            else:
                return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

def librarybooks(request):
    if request.method == "GET":
        try:
            data = JSONParser().parse(request)
            library_uid = None
            page = None
            size = None
            show_all = None
            if 'size' in data:
                size = data['size']
            if 'page' in data:
                page = data['page']
            if 'show_all' in data:
                show_all = data['show_all']
            if page is not None and size is not None:
                pass # ???
            if show_all is not None:
                pass # ???

            if 'library_uid' in data:
                library_uid = data['library_uid']
            else:
                return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

            return JsonResponse(q.get_library_books(library_uid), safe=False, status=status.HTTP_200_OK)


        except Exception as ex:
            print(ex)
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
    