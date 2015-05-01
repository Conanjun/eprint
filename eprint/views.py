# -*- coding=utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from dashboard.models import UserProfile

class UserRegForm(forms.Form):
    email = forms.EmailField(label='email', widget=forms.widgets.TextInput())
    password = forms.CharField(label='password', widget=forms.PasswordInput())
    phonenumber = forms.CharField(label='phonenumber', max_length=50)
    building = forms.CharField(label='building', max_length=4)


class UserLoginForm(forms.Form):
    email = forms.EmailField(label='email', widget=forms.widgets.TextInput())
    password = forms.CharField(label='password', widget=forms.PasswordInput())


def home(request):
    context = RequestContext(request)
    return render_to_response('index.html', context)


def register(request):
    context = RequestContext(request)
    return render_to_response('register.html', context)


def user_login(request):
    if request.method == 'POST':
        uf = UserLoginForm(request.POST)
        print request.POST

        if uf.is_valid():
            print 'enter the is_valid'
            #get the form's parameters
            email = uf.cleaned_data['email']
            user = User.objects.get(email=email)
            password = uf.cleaned_data['password']
            user = authenticate(username=user.username, password=password)
            if user is not None:
                login(request, user)
                user_prifile = UserProfile(user=user)
                return HttpResponse('Ok login')
        else:
            uf = UserLoginForm()
            return HttpResponseRedirect('/')


def contact(request):
    return HttpResponse('Contact us by email: hackeris@qq.com')


#register api
def api_register(request):
    print 'register had been attached'
    if request.method == 'POST':
        uf = UserRegForm(request.POST)
        if uf.is_valid():
            #get the form's parameters
            email = uf.cleaned_data['email']
            password = uf.cleaned_data['password']
            phonenumber = uf.cleaned_data['phonenumber']
            building = uf.cleaned_data['building']
            check_exist = User.objects.filter(email=email)
            if check_exist:
                return HttpResponse('Email address has been registered.')
            user = User()
            user_profile = UserProfile()  #   Other data for user
            user.email = email
            user.set_password(password)
            user.save()
            user_profile.user = user
            user_profile.phone_number = phonenumber
            user_profile.building = building
            user_profile.save()
            return HttpResponse('register success!')
    else:
        uf = UserRegForm()
    #return render_to_response('my_print.html',{'uf':uf}, context_instance=RequestContext(req))
    return HttpResponseRedirect('/dashboard')
