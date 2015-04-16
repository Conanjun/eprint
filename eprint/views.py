from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from django.shortcuts import RequestContext
from django.shortcuts import HttpResponseRedirect

def home(request):
	context = RequestContext(request)
	return render_to_response('index.html',context)

def register(request):
	context = RequestContext(request)
	return render_to_response('register.html',context)	

def user_login(request):
	if request.POST:
		return HttpResponse('Ok')
	else:
		return HttpResponseRedirect('/')

def contact(request):
	return HttpResponse('Contact us by email: hackeris@qq.com')
