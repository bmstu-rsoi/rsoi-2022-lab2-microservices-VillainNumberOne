from django.urls import re_path
from api import views

urlpatterns = [
    re_path(r'^api/v1/ratings$', views.rating_system_api),
    re_path(r'^api/v1/ratings/([a-zA-Z]+)$', views.rating_system_api),
]