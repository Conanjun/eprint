# Create your views here.
# Create your views here.
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from django.shortcuts import RequestContext
from django.shortcuts import HttpResponseRedirect

from django import forms
#from django.views.decorators.csrf import csrf_protect
#from print.models import UpFile


def have_try(request):
    return HttpResponse('Have try')

def upfile(request):
    return HttpResponse('upload successfuly')