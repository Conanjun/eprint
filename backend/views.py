# -*- coding=utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django import forms
from django.contrib.auth import login, authenticate
from order.models import *
from django.core.servers.basehttp import FileWrapper
import os


class AdminLoginForm(forms.Form):
    email = forms.EmailField(label='email', widget=forms.widgets.TextInput())
    password = forms.CharField(label='password', widget=forms.PasswordInput())


def show_login_page(request):
    context = RequestContext(request)
    return render_to_response('admin/login.html', context)


def admin_login(request):
    if request.method == 'POST':
        return perform_admin_login(request)
    else:
        return show_login_page(request)


def perform_admin_login(request):
    admin_form = AdminLoginForm(request.POST)
    if admin_form.is_valid():
        email = admin_form.cleaned_data['email']
        password = admin_form.cleaned_data['password']
        try:
            admin_user = User.objects.get(email=email)
        except:
            return show_login_page(request)
        admin_user_auth = authenticate(username=admin_user.username, password=password)
        if admin_user_auth.is_staff:
            login(request, admin_user_auth)
            return HttpResponseRedirect('../index')
        else:
            return show_login_page(request)
    else:
        return show_login_page(request)


def admin_index(request):
    if request.user.is_staff:
        context = RequestContext(request)
        return render_to_response('admin/index.html', context)
    else:
        return HttpResponseRedirect('login')


def admin_print_orders(request):
    if request.user.is_staff:
        context = RequestContext(request)
        print_orders_list = PrintOrder.objects.order_by("time")
        for orders in print_orders_list:
            print orders.user.email
        context['orders_list'] = print_orders_list
        # {"orders_list": print_orders_list}
        return render_to_response('admin/print_orders.html', context)
    else:
        return HttpResponseRedirect('login')


def admin_trial_orders(request):
    if request.user.is_staff:
        context = RequestContext(request)
        trial_orders_list = TrialOrder.objects.order_by("name")
        context['trial_orders_list'] = trial_orders_list
        return render_to_response('admin/trial_orders.html', context)
    else:
        return HttpResponseRedirect('login')


def download_files(request):
    if request.method == 'POST' and request.POST.has_key('btn'):
        path = request.path.split('/')
        filename = path[-2] + '/' + path[-1] #upfiles/main.cpp
        wrapper = FileWrapper(file(filename))
        response = HttpResponse(wrapper, content_type='text/plain')
        response['Content-Length'] = os.path.getsize(filename)
        response['Content-Encoding'] = 'utf-8'
        response['Content-Disposition'] = 'attachment;filename=%s' % filename
        return response
    else:
        return HttpResponse('download failed')