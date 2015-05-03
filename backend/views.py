# -*- coding=utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_protect


class AdminLoginForm(forms.Form):
    email = forms.EmailField(label='email', widget=forms.widgets.TextInput())
    password = forms.CharField(label='password', widget=forms.PasswordInput())


def admin_login(request):
    context = RequestContext(request)
    return render_to_response('admin_login.html',context)

def api_admin_login(request):
    if request.method == 'POST':
        admin_form = AdminLoginForm(request.POST)
        if admin_form.is_valid():
            email = admin_form.cleaned_data['email']
            password = admin_form.cleaned_data['password']
            admin_user = User.objects.get(email=email)
            admin_user_auth = authenticate(username = admin_user.username, password=password)
            if admin_user_auth.is_staff is True:
                login(request, admin_user_auth)
                return HttpResponse('Login Ok')
            else:
                return HttpResponse('Login fail')
    else:
        admin_form = AdminLoginForm()
    return HttpResponse('Login fail')
    #return HttpResponseRedirect('/backend/login')
