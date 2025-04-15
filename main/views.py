from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import CourseTitle, StudentProfile
from .forms import StudentRegistrationForm

def index(response):
    return render(response, 'main/base.html', {})

def home(response):
    return render(response, 'main/home.html', {})

def course_list(request):
    courses = CourseTitle.objects.all()
    print(courses)  # Debug line
    return render(request, 'main/course_list.html', {'courses':courses})

def register(request):
    form = StudentRegistrationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            level = form.cleaned_data.get('level')  # Get the level from the form
            student_profile = StudentProfile.objects.create(user=user, level=level)  
            return redirect('home')
        else:
            pass
    return render(request, 'main/register.html', {'form': form})
