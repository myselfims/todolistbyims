from datetime import date
import email
from operator import index
from django.db import models

# Create your models here.
class Task(models.Model):
    number = models.AutoField(primary_key=True)
    email = models.CharField(max_length=500,default="")
    task = models.CharField(max_length=5000,default="")
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.task
    
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500,default="")
    email = models.CharField(max_length=500,default="")
    password = models.CharField(max_length=8)