from django.db import models

# Create your models here.

class user_data(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postalcode = models.IntegerField
    country = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField
