#-*- coding=utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from django.shortcuts import RequestContext

#from django.shortcuts import HttpResponseRedirect

from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from dashboard.models import User #there may be some problems

class UserRegForm(forms.Form): 
    '''
    email=models.EmailField()
    password = models.CharField(max_length=50)
    phonenumber=models.CharField(max_length=50)
    building=models.CharField(max_length=4)

    '''
    email = forms.EmailField(label='email',widget=forms.widgets.TextInput())
    password = forms.CharField(label='password',widget=forms.PasswordInput())
    phonenumber=forms.CharField(label='phonenumber',max_length=50)
    building=forms.CharField(label='building',max_length=4)

class UserLoginForm(forms.Form):
    email = forms.EmailField(label='email',widget=forms.widgets.TextInput())
    password = forms.CharField(label='password',widget=forms.PasswordInput())    


def home(request):
    context = RequestContext(request)
    return render_to_response('index.html',context)

def register(request):
    context = RequestContext(request)
    return render_to_response('register.html',context)	
    
#problem needed to solved: return the current user in RedirectResponse
def user_login(request):
    if request.method=='POST':
	uf = UserLoginForm(request.POST)
	print request.POST

	if uf.is_valid():
	    print 'enter the is_valid'
	    #get the form's parameters
	    email = uf.cleaned_data['email']
	    password = uf.cleaned_data['password']
	    #compare with the data in database
	    user = User.objects.filter(email=email,password=password)
	    if user:
		# exists the user
		#return HttpResponse('Login Successfully')
		response = HttpResponseRedirect('dashboard')
		#write cookie
		response.set_cookie('email',email,3600)
		return response
	    else:
		# not exists the user
		return HttpResponse('Login Failly')
		#return HttpResponseRedirect('/')
	else:
	    uf = UserForm()
	    return HttpResponseRedirect('/')
	    #return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(req))	    
	    
		#return HttpResponse('Ok')
	#else:
		#return HttpResponseRedirect('/')

def contact(request):
	return HttpResponse('Contact us by email: hackeris@qq.com')

#register api
def api_register(request):
    print 'register had been attached'
    if request.method == 'POST':
	uf = UserRegForm(request.POST)
	if uf.is_valid():
	    #get the form's parameters
	    email = uf.cleaned_data['email']
	    password = uf.cleaned_data['password']
	    phonenumber=uf.cleaned_data['phonenumber']
	    building=uf.cleaned_data['building']
	    #add to the database
	    #here need to check the database whether there exists the same mail
	    #check_exist = User.query.filter_by(email=email).first()
	    check_exist=User.objects.filter(email=email)
	    if check_exist:
		return HttpResponse('Email address has been registered.')	   
	    User.objects.create(email=email,password=password,phonenumber=phonenumber,building=building)
	    #return HttpResponse('register success!')
    else:
	uf = UserForm()
    #return render_to_response('my_print.html',{'uf':uf}, context_instance=RequestContext(req))
    return HttpResponseRedirect('/dashboard')
