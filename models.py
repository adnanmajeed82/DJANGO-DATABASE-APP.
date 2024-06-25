# fruit_prices/models.py

from django.db import models

class Fruit(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Price(models.Model):
    fruit = models.ForeignKey(Fruit, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fruit.name} - {self.price} ({self.recorded_at})"
