from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def test(response):
    return HttpResponse("testing")
