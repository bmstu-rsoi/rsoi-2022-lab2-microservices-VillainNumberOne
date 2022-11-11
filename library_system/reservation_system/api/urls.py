from django.urls import re_path
from api import views

urlpatterns = [
    re_path(r'^api/v1/persons$', views.reservation_system_api),
    re_path(r'^api/v1/persons/([0-9]+)$', views.reservation_system_api),
]