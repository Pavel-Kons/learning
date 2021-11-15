from django.db import models

# Create your models here.


class Stock(models.Model):
	name = models.CharField(max_length=40)
	ticker = models.CharField(max_length=4, default="NULL")


class Currency(models.Model):
	name = models.CharField(max_length=40)