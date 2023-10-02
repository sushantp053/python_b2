from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=50,)
    desc = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField(default= 0)

    def __str__(self) -> str:
        return self.name
