from django.urls import re_path
from api import views

urlpatterns = [
    re_path(r'^api/v1/libraries$', views.libraries),
    re_path(r'^api/v1/librarybooks$', views.librarybooks),
    # re_path(r'^api/v1/libraries/([a-zA-Z]+)$', views.library_system_api),
]