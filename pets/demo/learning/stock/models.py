from django.db import models

# Create your models here.


class Stock(models.Model):
    name = models.CharField(max_length=40)
    ticker = models.CharField(max_length=4, default="NULL")\
    description = models.TextField(null=True, blank=True)


class Currency(models.Model):
    name = models.CharField(max_length=40)