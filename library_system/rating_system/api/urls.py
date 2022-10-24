from django.urls import re_path
from api import views

urlpatterns = [
    re_path(r'^api/v1/person$', views.rating_system_api),
    re_path(r'^api/v1/person/([0-9]+)$', views.rating_system_api),
]