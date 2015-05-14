# -*- coding=utf-8 -*-
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

    @staticmethod
    def get_status_of(order):
        if order.status == OrderStatus.STATUS_UPLOADED:
            return u'已上传'
        elif order.status == OrderStatus.STATUS_DOWNLOADED:
            return u'已下载'
        elif order.status == OrderStatus.STATUS_PRINTED:
            return u'已打印'
        elif order.status == OrderStatus.STATUS_FINISHED:
            return u'已完成'
        else:
            return None


class PrintMethod():
    def __init__(self):
        pass

    PRINT_COLORFUL = 0x0
    PRINT_BLACK_WHITE = 0x1

    @staticmethod
    def get_method_print_of(order):
        if order.color == PrintMethod.PRINT_COLORFUL:
            return u'彩印'
        elif order.color == PrintMethod.PRINT_BLACK_WHITE:
            return u'黑白'
        else:
            return None


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