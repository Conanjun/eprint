from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from django.shortcuts import RequestContext

def home(request):
	context = RequestContext(request)
	return render_to_response('index.html',context)

def register(request):
	context = RequestContext(request)
	return render_to_response('register.html',context)	
