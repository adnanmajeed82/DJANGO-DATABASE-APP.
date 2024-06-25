# fruit_prices/views.py

from django.shortcuts import render
from .models import Fruit, Price

def fruit_prices_list(request):
    fruits = Fruit.objects.all()
    context = {'fruits': fruits}
    return render(request, 'fruit_prices/fruit_prices_list.html', context)
