from django.urls import re_path
from api import views

urlpatterns = [
    re_path(r'^api/v1/persons$', views.library_system_api),
    re_path(r'^api/v1/persons/([0-9]+)$', views.library_system_api),
]