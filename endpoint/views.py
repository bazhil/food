# coding: utf-8
from .serializers import FoodListSerializer
from .models import Food, FoodCategory

from rest_framework import generics
from django.db.models import Prefetch


# Create your views here.
class FoodAPIList(generics.ListCreateAPIView):
    queryset = FoodCategory.objects.filter().prefetch_related(
        Prefetch('food', queryset=Food.objects.filter(is_publish=True))).order_by('id')

    serializer_class = FoodListSerializer

