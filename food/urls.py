# coding: utf-8

from django.contrib import admin
from django.urls import path
from endpoint.views import FoodAPIList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/foods/', FoodAPIList.as_view()),
]
