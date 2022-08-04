from datetime import date
import email
from operator import index
from unicodedata import name
from django.db import models

# Create your models here.
class Task(models.Model):
    number = models.AutoField(primary_key=True)
    username = models.CharField(max_length=500,default="")
    task = models.CharField(max_length=5000,default="")
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.task
    
