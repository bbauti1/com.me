from django.db import models

# Create your models here.

class Student(models.Model):
    dni = models.CharField(max_length=30)
    nroCarnet = models.CharField(max_length=30)
    username = models.IntegerField()
    vista = models.CharField(max_length=40)