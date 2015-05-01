from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from eprint.settings import MEDIA_ROOT

# Create your models here.


class PrintOrder(models.Model):
    user = models.ForeignKey(User)
    up_file = models.FileField(upload_to="upfiles/")
    time = models.DateTimeField()
    status = models.IntegerField()

    def __unicode__(self):
        return self.upfile.name

class TrialOrder(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    building = models.CharField(max_length=50)
    file = models.FileField(upload_to="upfiles/")

    def __unicode__(self):
        return self.file.name

