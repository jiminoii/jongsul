from django.db import models

class Food_Point(models.Model):
    title = models.CharField(max_length=100) 
    location = models.CharField(max_length=120, null=True)     
    tel = models.CharField(max_length=120, null=True)     
    lat = models.FloatField()
    lng = models.FloatField()
