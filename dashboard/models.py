from django.db import models

# Create your models here.

#user model: email password phonenumber building
class User(models.Model):
    #username = models.CharField(max_length=50)
    email=models.EmailField()
    password = models.CharField(max_length=50)
    phonenumber=models.CharField(max_length=50)
    building=models.CharField(max_length=4)


