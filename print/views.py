# Create your views here.
# Create your views here.
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from django.shortcuts import RequestContext
from django.shortcuts import HttpResponseRedirect


def have_try(request):
    return HttpResponse('Have try')

