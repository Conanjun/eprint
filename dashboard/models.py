from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
# Create your models here.


class BuildingGroup(models.Model):
    name = models.CharField(max_length=20)


class Building(models.Model):
    group = models.ForeignKey(BuildingGroup)
    name = models.CharField(max_length=20)


def get_grouped_buildings():
    return BuildingGroup.objects.all()


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=9)
    phone_number = models.CharField(max_length=20)
    building = models.ForeignKey(Building)
    gender = models.IntegerField()
    number = models.CharField(max_length=15)

    def can_use(self):
        if self.phone_number:
            return True
        else:
            return False


admin.site.register(BuildingGroup)
admin.site.register(Building)
