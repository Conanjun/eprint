from django.shortcuts import HttpResponse
from models import TrialOrder
from models import PrintOrder
from models import OrderStatus
from eprint.views import show_success
import datetime
from django import forms
from eprint import validate
from django.utils.html import escape


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
        print request.POST
        order = PrintOrderForm(request.POST, request.FILES)
        if order.is_valid():
            user = request.user
            new_print_order = PrintOrder()

            new_print_order.user = user
            new_print_order.up_file = order.cleaned_data['file']
            new_print_order.time = datetime.datetime.now()
            new_print_order.status = OrderStatus().STATUS_UPLOADED

            new_print_order.color = order.cleaned_data['color']
            new_print_order.method = order.cleaned_data['method']
            new_print_order.tel = escape(order.cleaned_data['tel'])

            if validate.print_order_validate['filetype'](new_print_order.up_file.name) and \
                    validate.print_order_validate['status'](new_print_order.status) and validate.print_order_validate[
                'method'](new_print_order.method):
                pass
            else:
                return show_success('upload fail', 'dashboard')

            new_print_order.save()
            return show_success('upload ok', 'dashboard')
    else:
        order = PrintOrderForm()
    return show_success('upload fail', 'dashboard')


def trial_order(request):
    file_obj = request.FILES.get('file', None)
    if request.method == "POST":
        uf = TrialOrderForm(request.POST, request.FILES)
        if uf.is_valid():
            new_trial_order = TrialOrder()
            new_trial_order.name = uf.cleaned_data['name']
            new_trial_order.phone = uf.cleaned_data['phone']
            new_trial_order.building = uf.cleaned_data['building']
            new_trial_order.file = uf.cleaned_data['file']
            new_trial_order.status = OrderStatus().STATUS_UPLOADED

            # print new_trial_order.file.name
            if validate.trial_order_validate['name'](new_trial_order.name) and validate.trial_order_validate['phone'](
                    new_trial_order.phone) and validate.trial_order_validate['building'](new_trial_order.building) and \
                    validate.trial_order_validate['filetype'](new_trial_order.file.name) and \
                    validate.trial_order_validate['status'](new_trial_order.status):
                pass
            else:
                return show_success('upload fail', '/')
            new_trial_order.save()
            return show_success('Upload ok', 'register')
    else:
        uf = TrialOrderForm()
    # return render_to_response('upfile.html',{'uf':uf})
    return show_success('upload fail', '/')
    # return HttpResponse('trail successfully')


def up_file(request):
    return HttpResponse('upload successfully')