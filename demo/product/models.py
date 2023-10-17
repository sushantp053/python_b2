from django.db import models
from django.contrib.auth.models import User
import uuid


class Product(models.Model):
    name = models.CharField(max_length=50,)
    desc = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name


class Address(models.Model):
    uid = models.UUIDField(primary_key=True, unique=True,
                           editable=False, default=uuid.uuid4)
    name = models.TextField()
    building_name = models.TextField(default="")
    flat = models.TextField()
    landmark = models.TextField()
    city = models.TextField()
    pin = models.IntegerField()
    mobile = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Cart(models.Model):
    uid = models.UUIDField(primary_key=True, unique=True,
                           editable=False, default=uuid.uuid4)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()
    total = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Order(models.Model):
    uid = models.UUIDField(primary_key=True, unique=True,
                           editable=False, default=uuid.uuid4)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()
    total = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    addr = models.ForeignKey(Address, on_delete=models.CASCADE)
