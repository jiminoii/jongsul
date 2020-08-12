from django.db import models

# Create your models here.
class Point(models.Model):
    title = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()

class Inpo(models.Model): #제가 몰라서 오타낸게 아닙니다 ㅠㅠㅠ
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)