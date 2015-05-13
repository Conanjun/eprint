# -*- coding=utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response, render_to_response
from django.shortcuts import HttpResponse, HttpResponseRedirect, RequestContext
from dashboard.models import UserProfile


def get_user_profile(user):
    user_profile = None
    try:
        user_profile = UserProfile.objects.get(user=user)
    except:
        user_profile = None
    return user_profile


def dashboard(request):
    user = request.user
    if user.is_authenticated():
        user_profile = get_user_profile(user)
        if not user_profile:
            user_profile = {}
        context = RequestContext(request)
        context['user_profile'] = user_profile
        return render_to_response('dashboard.html', context)
    else:
        return HttpResponseRedirect('/login')


def update_profile(request):
    user = request.user
    if user.is_authenticated():
        name = request.GET['name']
        phone = request.GET['phone']
        student_number = request.GET['student_number']
        building = request.GET['building']
        gender = request.GET['gender']

        user_profile = get_user_profile(user)
        if not user_profile:
            user_profile = UserProfile()
            user_profile.user = user
        user_profile.name = name
        user_profile.phone_number = phone
        user_profile.building = building
        user_profile.gender = gender
        user_profile.number = student_number
        user_profile.save()
        return HttpResponseRedirect('/dashboard')
    else:
        return HttpResponseRedirect('/login')
