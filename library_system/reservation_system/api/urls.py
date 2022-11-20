from django.urls import re_path
from api import views

urlpatterns = [
    re_path(r'^api/v1/reservations/(?P<username>[A-Za-z0-9_]+)$', views.get_user_reservations),
]