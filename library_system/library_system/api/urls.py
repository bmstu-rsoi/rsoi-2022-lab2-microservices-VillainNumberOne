from django.urls import re_path
from api import views

urlpatterns = [
    re_path(r'^api/v1/libraries$', views.library_system_api),
    re_path(r'^api/v1/libraries/([a-zA-Z]+)$', views.library_system_api),
]