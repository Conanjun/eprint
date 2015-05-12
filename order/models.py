from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
import datetime

admin.autodiscover()


class OrderStatus():
    def __init__(self):
        pass

    STATUS_UPLOADED = 0x1
    STATUS_DOWNLOADED = 0x2
    STATUS_PRINTED = 0x3
    STATUS_FINISHED = 0x4


class PrintOrder(models.Model):
    user = models.ForeignKey(User)
    up_file = models.FileField(upload_to="upfiles/")
    time = models.DateTimeField(default=datetime.datetime.now())
    status = models.IntegerField()
    color = models.IntegerField()
    method = models.IntegerField()

    def __unicode__(self):
        return self.up_file.name


class TrialOrder(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    time = models.DateTimeField(default=datetime.datetime.now())
    building = models.CharField(max_length=50)
    file = models.FileField(upload_to="upfiles/")
    status = models.IntegerField()

    def __unicode__(self):
        return self.file.name


class PrintOrderAdmin(admin.ModelAdmin):
    pass


class TrialOrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(PrintOrder, PrintOrderAdmin)
admin.site.register(TrialOrder, TrialOrderAdmin)