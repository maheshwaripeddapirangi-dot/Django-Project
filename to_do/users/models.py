from django.db import models

class Users(models.Model):
    name=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=15)
    address=models.CharField(max_length=100)
    role=models.CharField(max_length=50)
    password=models.CharField(max_length=15,default='M@ha8125')

# Create your models here.
