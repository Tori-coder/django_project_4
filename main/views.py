from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import CourseTitle, StudentProfile
from .forms import StudentRegistrationForm, StudentProfileForm, UserForm

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

def student_profile(request):
    profile = StudentProfile.objects.get(user=request.user)
    return render(request, 'main/profile.html', {'profile': profile})

def edit_profile(request):
    profile = StudentProfile.objects.get(user=request.user)
    if request.method == 'GET':
        user_form = UserForm(instance=request.user)
        profile_form = StudentProfileForm(instance=profile)
    else:
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = StudentProfileForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('student_profile')
    return render(request, 'main/edit_profile.html', {'user_form': user_form,'profile_form': profile_form,})

def delete_profile(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('home')