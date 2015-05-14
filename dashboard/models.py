from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BuildingGroup(models.Model):
    name = models.CharField(max_length=20)


class Building(models.Model):
    group = models.ForeignKey(BuildingGroup)
    name = models.CharField(max_length=20)


def get_buildings():
    return BuildingGroup.objects.all()


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=9)
    phone_number = models.CharField(max_length=20)
    building = models.ForeignKey(Building)
    gender = models.IntegerField()
    number = models.CharField(max_length=15)

