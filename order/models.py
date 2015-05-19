# -*- coding=utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
import datetime
from dashboard.models import UserProfile, Building

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
            return u'交易成功'
        else:
            return None


class PrintColor():
    def __init__(self):
        pass

    PRINT_COLORFUL = 0x0
    PRINT_BLACK_WHITE = 0x1

    @staticmethod
    def get_print_color_of(order):
        if order.color == PrintColor.PRINT_COLORFUL:
            return u'彩印'
        elif order.color == PrintColor.PRINT_BLACK_WHITE:
            return u'黑白'
        else:
            return None


class PrintMethod():
    def __init__(self):
        pass

    PAID_PRINT = 0x1
    FREE_PRINT = 0x2

    @staticmethod
    def get_print_method(order):
        if order.method == PrintMethod.PAID_PRINT:
            return u'付费打印'
        elif order.method == PrintMethod.FREE_PRINT:
            return u'免费打印'
        else:
            return None


class PrintOrder(models.Model):
    user = models.ForeignKey(User)
    up_file = models.FileField(upload_to="upfiles/")
    time = models.DateTimeField(default=datetime.datetime.now())
    status = models.IntegerField()
    color = models.IntegerField()
    method = models.IntegerField()
    comment = models.TextField()

    def __unicode__(self):
        return self.up_file.name

    def get_user(self):
        profile = UserProfile.objects.get(user=self.user)
        return profile.name

    def get_user_phone(self):
        profile = UserProfile.objects.get(user=self.user)
        return profile.phone_number

    def get_status(self):
        return OrderStatus.get_status_of(self)

    def get_print_color_of(self):
        return PrintColor.get_print_color_of(self)

    def get_file_name(self):
        return self.up_file.name.split('/')[1]

    def get_building(self):
        profile = UserProfile.objects.get(user=self.user)
        return profile.building.name


class TrialOrder(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    time = models.DateTimeField(default=datetime.datetime.now())
    building = models.CharField(max_length=50)
    up_file = models.FileField(upload_to="upfiles/")
    status = models.IntegerField()

    def __unicode__(self):
        return self.file.name

    def get_status(self):
        return OrderStatus.get_status_of(self)
        
    def get_file_name(self):
        return self.up_file.name.split('/')[1]

    @staticmethod
    def is_this_phone_used(phone):
        trial_orders = TrialOrder.objects.filter(phone=phone)
        if not trial_orders:
            return False
        else:
            return True


class PrintOrderAdmin(admin.ModelAdmin):
    pass


class TrialOrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(PrintOrder, PrintOrderAdmin)
admin.site.register(TrialOrder, TrialOrderAdmin)