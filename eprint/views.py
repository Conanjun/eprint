# -*- coding=utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from dashboard.models import UserProfile
from dashboard.models import get_grouped_buildings


def authenticated_view(func):
    def _deco(*args, **kwargs):
        user = args[0].user
        if user.is_authenticated():
            ret = func(*args, **kwargs)
            return ret
        else:
            return HttpResponseRedirect('/login')

    return _deco


class UserRegForm(forms.Form):
    email = forms.EmailField(label='email', widget=forms.widgets.TextInput())
    name = forms.CharField(label='name', widget=forms.widgets.TextInput())
    password = forms.CharField(label='password', widget=forms.PasswordInput())
    phone_number = forms.CharField(label='phone_number', max_length=50)
    building = forms.CharField(label='building', max_length=4)


class UserLoginForm(forms.Form):
    email = forms.EmailField(label='email', widget=forms.widgets.TextInput())
    password = forms.CharField(label='password', widget=forms.PasswordInput())


def home(request):
    context = RequestContext(request)
    return render_to_response('index.html', context)


def perform_user_register(request):
    err = ''
    uf = UserRegForm(request.POST)
    if uf.is_valid():
        email = uf.cleaned_data['email']
        name = uf.cleaned_data['name']
        password = uf.cleaned_data['password']
        phone_number = uf.cleaned_data['phone_number']
        building = uf.cleaned_data['building']
        check_exist = User.objects.filter(email=email)
        if check_exist:
            err = 'exist'
        user = User()
        user_profile = UserProfile()  # Other data for user
        user.email = email
        user.name = name
        user.set_password(password)
        user.save()
        user_profile.user = user
        user_profile.phone_number = phone_number
        user_profile.building = building
        user_profile.save()
        return HttpResponseRedirect('login')
    else:
        context = RequestContext(request)
        return render_to_response('register.html', context)


def register(request):
    if request.method == 'POST':
        return perform_user_register(request)
    else:
        context = RequestContext(request)
        context['groups'] = get_grouped_buildings()
        return render_to_response('register.html', context)


def user_login(request):
    if request.method == 'POST':
        uf = UserLoginForm(request.POST)
        if uf.is_valid():
            email = uf.cleaned_data['email']
            user = User.objects.get(email=email)
            password = uf.cleaned_data['password']
            user = authenticate(username=user.username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


@authenticated_view
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def contact(request):
    return HttpResponse('Contact us by email: hackeris@qq.com')


def show_success(message='Success', redir=''):
    context = {'message': message, 'redir': redir}
    return render_to_response('success.html', context)

