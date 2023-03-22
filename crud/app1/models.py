from django.db import models

class Person(models.Model):
    name= models.CharField(max_length=50)
    email= models.EmailField()
    location= models.CharField(max_length=50,blank=True)
# Create your models here.
