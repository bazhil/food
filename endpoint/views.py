# coding: utf-8
from .serializers import FoodListSerializer
from .models import Food, FoodCategory

from rest_framework import generics
from django.db.models import Prefetch


# Create your views here.
class FoodAPIList(generics.ListCreateAPIView):
    food_queryset = Food.objects.filter(is_publish=True)
    queryset = FoodCategory.objects.filter(food__is_publish=True).prefetch_related(
        Prefetch('food', queryset=food_queryset)).order_by('id')

    serializer_class = FoodListSerializer

