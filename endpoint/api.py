# coding: utf-8
from .models import Food, FoodCategory
from rest_framework import viewsets, permissions
from .serializers import FoodSerializer, FoodListSerializer


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.filter(is_publish=True)
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FoodSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = FoodCategory.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FoodListSerializer