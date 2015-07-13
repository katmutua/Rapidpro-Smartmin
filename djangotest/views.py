from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render 

def index(request):
    response = "Logged out of application!"
    return HttpResponse(response)

def home(request):
		return render(request, 'home.html', dirs=('templates',)) 



