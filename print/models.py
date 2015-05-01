from django.db import models
from django.db import models
from django.contrib import admin
from eprint.settings import MEDIA_ROOT

# Create your models here.


class UpFile(models.Model):
    username = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    up_file = models.FileField(upload_to="upfiles/")
    building = models.CharField(max_length=4)

    def __unicode__(self):
        return self.upfile.name