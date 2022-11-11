from hashlib import new
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse, HttpResponse
from rest_framework import status

from api.models import  Rating
from api.serializers import  RatingSerializer
from api.messages import *


@csrf_exempt
def rating_system_api(request, id=None):
    if request.method == "GET":
        if id is None:
            ratings =  Rating.objects.all()
            ratings_serializer =  RatingSerializer(ratings, many=True)
            return JsonResponse(ratings_serializer.data, safe=False, status=status.HTTP_200_OK)
        else:
            pass
            # try:
            #     person =  Rating.objects.get(id=id)
            #     person_serializer =  RatingSerializer(person)
            #     return JsonResponse(person_serializer.data, safe=False, status=status.HTTP_200_OK)
            # except  Rating.DoesNotExist:
            #     return HttpResponse(status=status.HTTP_404_NOT_FOUND)


