# from django.conf.urls import url
from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^create/$', views.order_create, name='order_create'),
]