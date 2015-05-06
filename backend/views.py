# -*- coding=utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_protect
from order import models as Order


class AdminLoginForm(forms.Form):
    email = forms.EmailField(label='email', widget=forms.widgets.TextInput())
    password = forms.CharField(label='password', widget=forms.PasswordInput())


def admin_login(request):
    context = RequestContext(request)
    return render_to_response('admin_login.html', context)


def api_admin_login(request):
    if request.method == 'POST':
        admin_form = AdminLoginForm(request.POST)
        if admin_form.is_valid():
            email = admin_form.cleaned_data['email']
            password = admin_form.cleaned_data['password']
            try:
                admin_user = User.objects.get(email=email)
            except:
                return HttpResponse('Login fail')
            admin_user_auth = authenticate(username=admin_user.username, password=password)
            if admin_user_auth.is_staff is True:
                login(request, admin_user_auth)
                return HttpResponseRedirect('../index')
                # return HttpResponse('Login Ok')
            else:
                return HttpResponse('Login fail')
    else:
        admin_form = AdminLoginForm()
    return HttpResponse('Login fail')
    # return HttpResponseRedirect('/backend/login')


def admin_index(request):
    if request.user.is_staff is True:
        context = RequestContext(request)
        return render_to_response('admin_index.html', context)
    else:
        return HttpResponseRedirect('login')


def admin_orders(request):
    if request.user.is_staff is True:
        context = RequestContext(request)
        return render_to_response('admin_index_orders.html', context)
        # return render_to_response('admin_index_orders.html',context,{"orders":orders})
    else:
        return HttpResponseRedirect('login')


def admin_print_orders(request):
    if request.user.is_staff is True:
        context = RequestContext(request)
        print_orders_list = Order.PrintOrder.objects.order_by("time")
        for orders in print_orders_list:
            print orders.user.email
        context['orders_list'] = print_orders_list
        # {"orders_list": print_orders_list}
        return render_to_response('admin_index_print_orders.html', context)
    else:
        return HttpResponseRedirect('login')


def admin_trial_orders(request):
    if request.user.is_staff is True:
        context = RequestContext(request)
        trial_orders_list = Order.TrialOrder.objects.order_by("name")
        context['trial_orders_list'] = trial_orders_list
        return render_to_response('admin_index_trial_orders.html', context)
    else:
        return HttpResponseRedirect('login')



