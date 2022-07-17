from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=20)
    score = models.IntegerField(default=0)
    identity = models.CharField(max_length=10)