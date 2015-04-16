# Create your views here.
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from django.shortcuts import RequestContext
from django.shortcuts import HttpResponseRedirect


def dashboard(request):
	return render_to_response('dashboard.html')
