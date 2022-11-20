from hashlib import new
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse, HttpResponse
from rest_framework import status

# from api.serializers import PersonSerializer
from api.messages import *

import api.services_requests
import api.utils.utils as utils
import api.errors as errors


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
                librarybooks = api.services_requests.get_library_books(library_uid)
                return JsonResponse(librarybooks, safe=False, status=status.HTTP_200_OK)
            except Exception as ex:
                print(ex)
                return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def reservations(request):
    if request.method == "GET":
        headers = utils.get_http_headers(request)
        if "X_USER_NAME" in headers.keys():
            username = headers["X_USER_NAME"]
            reservations = api.services_requests.get_user_reservations(username)
            return JsonResponse(reservations, safe=False, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        headers = utils.get_http_headers(request)
        if "X_USER_NAME" in headers.keys():
            username = headers["X_USER_NAME"]
        else:
            return JsonResponse(errors.reservations_no_username(), status=status.HTTP_400_BAD_REQUEST)

        try:
            data = JSONParser().parse(request)
            if all(k in data for k in ['bookUid', 'libraryUid', 'tillDate']):
                book_uid = data['bookUid']
                library_uid = data['libraryUid']
                till_date = data['tillDate']
            else:
                return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            print(ex)
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

        try:
            result = api.services_requests.make_reservation(username, book_uid, library_uid, till_date)
        except Exception as ex:
            return HttpResponse(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if result is not None:
            return JsonResponse(result, safe=False, status=status.HTTP_200_OK)
        else:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    return HttpResponse(status=status.HTTP_400_BAD_REQUEST)