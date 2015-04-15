from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse

def home(request):
	return render_to_response('index.html')
