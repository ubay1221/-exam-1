from django.db import models


class Taxi(models.Model):
    name = models.CharField(max_length=100)
    plate = models.TextField()
    d_name = models.IntegerField()
    model = models.TextField()
    stat = models.TextField()
