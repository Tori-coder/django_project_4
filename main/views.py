from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import CourseTitle

def index(response):
    return render(response, 'main/base.html', {})

def home(response):
    return render(response, 'main/home.html', {})

def course_list(request):
    courses = CourseTitle.objects.all()
    print(courses)  # Debug line
    return render(request, 'main/course_list.html', {'courses':courses})