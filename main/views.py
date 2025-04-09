from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def index(response):
    return render(response, 'main/base.html', {})

def home(response):
    return render(response, 'main/home.html', {})