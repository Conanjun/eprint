# -*- coding=utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django import forms
from django.contrib.auth import login, authenticate
from order.models import *
from django.core.servers.basehttp import FileWrapper
import os


def staff_view(func):
    def _deco(*args, **kwargs):
        if args[0].user.is_staff:
            ret = func(*args, **kwargs)
            return ret
        else:
            return HttpResponseRedirect('/backend/login')

    return _deco


class BackendLoginForm(forms.Form):
    email = forms.EmailField(label='email', widget=forms.widgets.TextInput())
    password = forms.CharField(label='password', widget=forms.PasswordInput())


def show_login_page(request):
    context = RequestContext(request)
    return render_to_response('backend/login.html', context)


def backend_login(request):
    if request.method == 'POST':
        return perform_backend_login(request)
    else:
        return show_login_page(request)


def perform_backend_login(request):
    backend_form = BackendLoginForm(request.POST)
    if backend_form.is_valid():
        email = backend_form.cleaned_data['email']
        password = backend_form.cleaned_data['password']
        try:
            backend_user = User.objects.get(email=email)
        except:
            return show_login_page(request)
        backend_user_auth = authenticate(username=backend_user.username, password=password)
        if backend_user_auth.is_staff:
            login(request, backend_user_auth)
            return HttpResponseRedirect('index')
        else:
            return show_login_page(request)
    else:
        return show_login_page(request)


def backend_index(request):
    context = RequestContext(request)
    return render_to_response('backend/index.html', context)


@staff_view
def backend_print_orders(request):
    context = RequestContext(request)
    print_orders_list = PrintOrder.objects.order_by("time")
    context['orders_list'] = print_orders_list
    return render_to_response('backend/print_orders.html', context)


@staff_view
def backend_trial_orders(request):
    context = RequestContext(request)
    trial_orders_list = TrialOrder.objects.order_by("name")
    context['trial_orders_list'] = trial_orders_list
    return render_to_response('backend/trial_orders.html', context)


@staff_view
def download_files(request, order_type, order_id):
    if request.method == 'POST' and request.POST.has_key('btn'):
        if order_type == 'print_order':
            order = PrintOrder.objects.get(id=order_id)
        elif order_type == 'trial_order':
            order = TrialOrder.objects.get(id=order_id)
        else:
            return HttpResponse('/backend/index')

        order.status = OrderStatus.STATUS_DOWNLOADED
        order.save()

        f = open(str(order.up_file), 'rb')
        data = f.read()
        f.close()
        response = HttpResponse(data, content_type='application/octet-stream')
        response['Content-Length'] = os.path.getsize(str(order.up_file))
        response['Content-Encoding'] = 'utf-8'
        response['Content-Disposition'] = 'attachment;filename=%s' % str(order.up_file).split('/')[1]
        return response
    else:
        return HttpResponse('download failed')