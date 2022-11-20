from hashlib import new
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse, HttpResponse
from rest_framework import status

from api.models import Reservation
from api.serializers import ReservationSerializer
from api.messages import *
import api.queries as q


@csrf_exempt
def get_user_reservations(request, username=None):
    if request.method == "GET":
        if username is not None:
            persons = Reservation.objects.filter(username=username).all()
            person_serializer = ReservationSerializer(persons, many=True)
            return JsonResponse(person_serializer.data, safe=False, status=status.HTTP_200_OK)

    return HttpResponse(status=status.HTTP_400_BAD_REQUEST) 

@csrf_exempt
def get_rented(request, username=None):
    if request.method == "GET":
        if username is not None:
            try:
                return JsonResponse(q.get_rented_count(username), safe=False, status=status.HTTP_200_OK)
            except Exception as ex:
                print(ex)
                return HttpResponse(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return HttpResponse(status=status.HTTP_400_BAD_REQUEST)