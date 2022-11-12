from django.urls import re_path
from api import views

urlpatterns = [
    re_path(r'^api/v1/libraries/$', views.libraries),
    re_path(r'^api/v1/libraries$', views.libraries),
    re_path(r'^api/v1/libraries/(?P<library_uid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/books$', views.libraries)
    # re_path(r'^api/v1/library_service/([0-9]+)$', views.gateway_api),
]