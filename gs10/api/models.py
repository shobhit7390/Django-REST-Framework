from django.db import models
from django.db.models.base import Model

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    roll=models.IntegerField()
    city=models.CharField(max_length=50)
