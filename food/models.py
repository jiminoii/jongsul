from django.db import models


class Food_Inpo(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)