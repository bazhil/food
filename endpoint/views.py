# coding: utf-8
from .serializers import FoodListSerializer
from .models import Food, FoodCategory

from rest_framework import generics
from django.db.models import Prefetch


# Create your views here.
class DjangoFilterBackend:
    pass


class FoodAPIList(generics.ListAPIView):
    queryset = FoodCategory.objects.filter(food__is_publish=True).prefetch_related(
        Prefetch('food', queryset=Food.objects.filter(is_publish=True))).distinct().order_by('id')

    serializer_class = FoodListSerializer
