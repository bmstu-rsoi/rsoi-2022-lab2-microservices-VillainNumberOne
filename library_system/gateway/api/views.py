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
def libraries(request, id=None):
    if request.method == "GET":
        if id is None:
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
                    pass

                if 'city' in data:
                    city = data['city']
                    try:
                        libraries_data = api.libraries_requests.get_city_libraries(city)
                        return JsonResponse(libraries_data, safe=False, status=status.HTTP_200_OK)
                    except Exception:
                        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
                else:
                    return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
            except:
                return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        else:
            pass
            # try:
            #     person = Person.objects.get(id=id)
            #     person_serializer = PersonSerializer(person)
            #     return JsonResponse(person_serializer.data, safe=False, status=status.HTTP_200_OK)
            # except Person.DoesNotExist:
            #     return HttpResponse(status=status.HTTP_404_NOT_FOUND)
