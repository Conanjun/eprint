# -*- coding=utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response, render_to_response
from django.shortcuts import HttpResponse, HttpResponseRedirect, RequestContext
from dashboard.models import UserProfile


def dashboard(request):
    user = request.user
    if user.is_authenticated():
    	context = RequestContext(request)
	    return render_to_response('dashboard.html', context)
	return HttpResponseRedirect('login')


def update_profile(request):
	user = request.user
	if user.is_authenticated():
		name = request.GET['name']
		tel = request.GET['tel']
		number = request.GET['number']
		building = request.GET['building']
		gender = request.GET['gender']

		user_profile = UserProfile.get(user=user)
		user_profile.phone_number = tel
		user_profile.building = building
		user_profile.gender = gender
		user_profile.number = number
		user_profile.save()
		return HttpResponseRedirect('dashboard')
	else:
		return HttpResponseRedirect('login')