from hashlib import new
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse, HttpResponse
from rest_framework import status

# from api.serializers import PersonSerializer
from api.messages import *

import api.libraries_requests


@csrf_exempt
def libraries(request, library_uid=None):
    if request.method == "GET":
        if library_uid is None:
            try:
                page = None
                size = None
                city = None
                if 'size' in request.GET:
                    size = request.GET['size']
                if 'page' in request.GET:
                    page = request.GET['page']
                if page is not None and size is not None:
                    pass

                if 'city' in request.GET:
                    city = request.GET['city']
                    try:
                        libraries_data = api.libraries_requests.get_city_libraries(city)
                        return JsonResponse(libraries_data, safe=False, status=status.HTTP_200_OK)
                    except Exception:
                        # Get response status
                        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
                else:
                    return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
            except:
                return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        else:
            page = None
            size = None
            show_all = None
            if 'size' in request.GET:
                size = request.GET['size']
            if 'page' in request.GET:
                page = request.GET['page']
            if page is not None and size is not None:
                pass # ???

            if 'showAll' in request.GET:
                show_all = request.GET['showAll']
            if show_all is not None:
                pass # ???
            
            try:
                librarybooks = api.libraries_requests.get_library_books(library_uid)
                return JsonResponse(librarybooks, safe=False, status=status.HTTP_200_OK)
            except Exception as ex:
                # print(ex)
                return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
