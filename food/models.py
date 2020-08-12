from django.db import models


class Food_Inpo(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)

# 음식점 상호 & 위치 
class Food_Point(models.Model):
    title = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()
