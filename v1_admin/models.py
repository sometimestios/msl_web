from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Host(models.Model):
    name=models.CharField(max_length=100)

class Log(models.Model):
    name=models.CharField(max_length=100)
    host=models.ForeignKey(Host,on_delete=models.CASCADE)
    body=models.TextField()
