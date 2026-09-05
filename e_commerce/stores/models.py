from django.db import models
class StoreDetails(models.Model):
    
    store_name=models.CharField(max_length=50)
    store_address=models.CharField(max_length=150)
    no_of_rooms=models.IntegerField()

# Create your models here.
