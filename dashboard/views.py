# -*- coding=utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response, render_to_response
from django.shortcuts import HttpResponse, HttpResponseRedirect, RequestContext
from dashboard.models import UserProfile
from eprint import validate


def get_user_profile(user):
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


def validate_user_profile(user_profile):
    if validate.update_profile_validate['name'](user_profile.name)\
            and validate.update_profile_validate['phone'](user_profile.phone)\
            and validate.update_profile_validate['student_number'](user_profile.number)\
            and validate.update_profile_validate['building'](user_profile.building)\
            and validate.update_profile_validate['gender'](user_profile.gender):
        return True
    return False


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

        if validate_user_profile(user_profile):
            user_profile.save()
            return HttpResponseRedirect('/dashboard')
        else:
            #   TODO: show error message here
            return HttpResponseRedirect('/dashboard')
    else:
        return HttpResponseRedirect('/login')
