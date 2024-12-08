from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=20)
    balance = models.DecimalField()
    age = models.IntegerField()


class Game(models.Model):
    title = models.CharField(max_length=50)
    cost = models.DecimalField()
    size = models.DecimalField()
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField()
