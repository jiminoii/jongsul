from django.db import models

class User(models.Model):
    id1 = models.CharField(max_length=10)
    pwd = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
