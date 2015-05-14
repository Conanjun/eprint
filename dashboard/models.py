from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=9)
    phone_number = models.CharField(max_length=20)
    building = models.CharField(max_length=4)
    gender = models.IntegerField()
    number = models.CharField(max_length=15)

