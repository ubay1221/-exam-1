from django.db import models


class Meal(models.Model):
    name = models.CharField(max_length=100)
    igredients = models.TextField()
    price = models.IntegerField()
    type = models.TextField()
    cuisine = models.TextField()
