from django.shortcuts import HttpResponse
from models import TrialOrder
from models import PrintOrder
from models import OrderStatus
import datetime

from django import forms


class PrintOrderForm(forms.Form):
    file = forms.FileField()
    color = forms.CharField()
    method = forms.CharField()
    tel = forms.CharField()


class TrialOrderForm(forms.Form):
    name = forms.CharField()
    phone = forms.CharField()
    building = forms.CharField()
    file = forms.FileField()


def have_try(request):
    return HttpResponse('Have try')


def print_order(request):
    if request.method == "POST":
        print 'enter the post compariation'
        print request.POST
        order = PrintOrderForm(request.POST, request.FILES)
        if order.is_valid():
            print 'enter the valid'
            user = request.user
            new_print_order = PrintOrder()

            # print_order.name= order.cleaned_data['name']
            new_print_order.user = user
            new_print_order.up_file = order.cleaned_data['file']
            new_print_order.time = datetime.datetime.now()
            new_print_order.status = OrderStatus().STATUS_UPLOADED

            new_print_order.color = order.cleaned_data['color']
            new_print_order.method = order.cleaned_data['method']
            new_print_order.tel = order.cleaned_data['tel']
            new_print_order.save()
            return HttpResponse('upload ok')
    else:
        order = PrintOrderForm()
    return HttpResponse('upload fail')


def trial_order(request):
    print 'enter the trial_order'
    print request.FILES
    print request.POST
    file_obj = request.FILES.get('file', None)
    print file_obj
    if request.method == "POST":
        print 'enter the post compariation'
        uf = TrialOrderForm(request.POST, request.FILES)
        if uf.is_valid():
            print 'enter the valid'
            new_trial_order = TrialOrder()
            new_trial_order.name = uf.cleaned_data['name']
            new_trial_order.phone = uf.cleaned_data['phone']
            new_trial_order.building = uf.cleaned_data['building']
            new_trial_order.file = uf.cleaned_data['file']
            new_trial_order.status = OrderStatus().STATUS_UPLOADED
            new_trial_order.save()
            return HttpResponse('upload ok!')
    else:
        uf = TrialOrderForm()
    # return render_to_response('upfile.html',{'uf':uf})
    return HttpResponse('upload fail')
    # return HttpResponse('trail successfully')


def up_file(request):
    return HttpResponse('upload successfully')