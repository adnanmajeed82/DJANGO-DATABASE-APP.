# fruit_prices/admin.py

from django.contrib import admin
from .models import Fruit, Price

# Register your models here.

@admin.register(Fruit)
class FruitAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('fruit', 'price', 'recorded_at')
