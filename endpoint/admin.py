from django.contrib import admin

# Register your models here.
from endpoint.models import Food, FoodCategory

admin.site.register(Food)
admin.site.register(FoodCategory)
