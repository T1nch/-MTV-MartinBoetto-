from django.db import models

class Familia(models.Model):
    nombre=models.CharField(max_length=40)
    edad=models.IntegerField()
    nacimiento= models.DateField(max_length=40)
