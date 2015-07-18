from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    response = "Spike"
    return HttpResponse(response)


def home(request):
    return render(request, 'home.html', dirs=('templates',))
