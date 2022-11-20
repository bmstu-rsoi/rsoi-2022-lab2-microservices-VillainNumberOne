from hashlib import new
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse, HttpResponse
from rest_framework import status

from api.models import Reservation
from api.serializers import ReservationSerializer
from api.messages import *


@csrf_exempt
def get_user_reservations(request, username=None):
    if request.method == "GET":
        if username is not None:
            persons = Reservation.objects.filter(username=username).all()
            person_serializer = ReservationSerializer(persons, many=True)
            return JsonResponse(person_serializer.data, safe=False, status=status.HTTP_200_OK)

    return HttpResponse(status=status.HTTP_400_BAD_REQUEST) 

    # elif request.method == "POST":
    #     try:
    #         new_person = JSONParser().parse(request)
    #     except:
    #         return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    #     person_serializer = ReservationSerializer(data=new_person)
    #     if person_serializer.is_valid():
    #         result = person_serializer.save()
    #         return HttpResponse(
    #             headers={"Location": f"/api/v1/persons/{result.id}"}, 
    #             status=status.HTTP_201_CREATED
    #         )
    #     else:
    #         return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    # elif request.method=='PATCH':
    #     updated_data = JSONParser().parse(request)
    #     try:
    #         person = Reservation.objects.get(id=id)
    #     except Reservation.DoesNotExist:
    #         return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    #     person_serializer = ReservationSerializer(person, data=updated_data)
    #     if person_serializer.is_valid():
    #         person_serializer.save()
    #         return JsonResponse(person_serializer.data, status=status.HTTP_200_OK)
    #     else:
    #         return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    # elif request.method=='DELETE':
    #     try:
    #         person = Reservation.objects.get(id=id)
    #     except Reservation.DoesNotExist:
    #         return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    #     person.delete()
    #     return HttpResponse(status=status.HTTP_204_NO_CONTENT)