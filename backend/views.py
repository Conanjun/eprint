# -*- coding=utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django import forms
from django.contrib.auth.models import User


def admin_login(request):
     return render_to_response('admin_login.html')
     #return HttpResponse('admin login ok')
