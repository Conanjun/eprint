# -*- coding=utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django import forms
from django.contrib.auth import login, authenticate
from order.models import *
from dashboard.views import download_file_response
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
    login_form = BackendLoginForm(request.POST)
    if login_form.is_valid():
        email = login_form.cleaned_data['email']
        password = login_form.cleaned_data['password']
        try:
            backend_user = User.objects.get(email=email)
        except:
            return show_login_page(request)
        backend_user_auth = authenticate(username=backend_user.username, password=password)
        if backend_user_auth.is_staff:
            login(request, backend_user_auth)
            return HttpResponseRedirect('/backend/index')
        else:
            return show_login_page(request)
    else:
        return show_login_page(request)


@staff_view
def backend_index(request):
    context = RequestContext(request)
    return render_to_response('backend/index.html', context)


@staff_view
def backend_trial_orders(request):
    context = RequestContext(request)
    trial_orders_list = TrialOrder.objects.order_by("time").reverse()
    context['trial_orders_list'] = trial_orders_list
    return render_to_response('backend/trial_orders.html', context)


@staff_view
def backend_print_orders(request):
    context = RequestContext(request)
    print_orders_list = PrintOrder.objects.filter(status=OrderStatus.STATUS_UPLOADED).order_by("time").reverse()
    context['orders_list'] = print_orders_list
    return render_to_response('backend/print_orders.html', context)


@staff_view
def backend_printed_orders(request):
    context = RequestContext(request)
    printed_orders_list = PrintOrder.objects.filter(status=OrderStatus.STATUS_PRINTED).order_by("time").reverse()
    context['printed_orders_list'] = printed_orders_list
    return render_to_response('backend/printed_orders.html', context)


@staff_view
def backend_finished_orders(request):
    context = RequestContext(request)
    finished_orders_list = PrintOrder.objects.filter(status=OrderStatus.STATUS_FINISHED).order_by("time").reverse()
    context['finished_orders_list'] = finished_orders_list
    return render_to_response('backend/finished_orders.html', context)


@staff_view
def download_files(request, order_type, order_id):

    if order_type == 'print_order':
        order = PrintOrder.objects.get(id=order_id)
    elif order_type == 'trial_order':
        order = TrialOrder.objects.get(id=order_id)
    else:
        return HttpResponseRedirect('/backend')

    order.status = OrderStatus.STATUS_DOWNLOADED
    order.save()

    return download_file_response(str(order.up_file))


@staff_view
def change_order_status(request, order_type, order_id, new_status):
    redirect_to = request.GET['redirect_to']
    if order_type == 'print_order':
        order = PrintOrder.objects.get(id=order_id)
    elif order_type == 'trial_order':
        order = TrialOrder.objects.get(id=order_id)
    else:
        return redirect(redirect_to)
    order.status = new_status
    order.save()
    return redirect(redirect_to)
