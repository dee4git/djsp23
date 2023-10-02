from django.db import models


# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(default=0.00)

    def __str__(self):
        return self.name
