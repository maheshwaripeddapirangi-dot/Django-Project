from django.db import models

class Users(models.Model):
    name=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=15)
    address=models.CharField(max_length=100)
    role=models.CharField(max_length=50)
    password=models.CharField(max_length=15)

class Courses(models.Model):
    course=models.CharField(max_length=20)
    description=models.TextField()
    Students=models.ManyToManyField(Users,related_name='course',blank=True)
  

# Create your models here.
