# fruit_price_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fruits/', include('fruit_prices.urls')),
]
