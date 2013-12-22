from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=100)


class Dish(models.Model):
    shop = models.ForeignKey('Shop')
    name = models.CharField(max_length=100)
    price = models.FloatField()


class Order(models.Model):
    device_id = models.CharField(max_length=50)
    date_time = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey('Order')
    dish = models.ForeignKey('Dish')
    count = models.IntegerField()
