# Create your views here.
# Create your views here.
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from django.shortcuts import RequestContext
from django.shortcuts import HttpResponseRedirect
from models import TrialOrder


from django import forms
#from django.views.decorators.csrf import csrf_protect
#from print.models import UpFile

class TrialOrderForm(forms.Form):
    name = forms.CharField()
    phone = forms.CharField()
    building = forms.CharField()
    file = forms.FileField()

def have_try(request):
    return HttpResponse('Have try')

def trial_order(request):
    print 'enter the trial_order'
    print request.FILES
    print request.POST
    file_obj = request.FILES.get('file',None)
    print file_obj
    if request.method == "POST":
        print 'enter the post compariation'
        uf = TrialOrderForm(request.POST, request.FILES)
        if uf.is_valid():
            print 'enter the valid'
            trial_order = TrialOrder()
            trial_order.name= uf.cleaned_data['name']
            trial_order.phone = uf.cleaned_data['phone']
            trial_order.building = uf.cleaned_data['building']
            trial_order.file = uf.cleaned_data['file']
            trial_order.save()
            return HttpResponse('upload ok!')
    else:
        uf =TrialOrderForm()
    #return render_to_response('upfile.html',{'uf':uf})
    return HttpResponse('upload fail')
    #return HttpResponse('trail successfully')

def up_file(request):
    return HttpResponse('upload successfully')