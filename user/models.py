from django.db import models

class User(models.Model):
    id1 = models.CharField(max_length=10)
    pwd = models.CharField(max_length=10)
    name = models.CharField(max_length=10)

class Board(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    id1 = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    title_num = models.ForeignKey(Board, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    content = models.CharField(max_length=500)