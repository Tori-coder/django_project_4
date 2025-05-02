from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import CourseTitle, StudentProfile, Enrolment
from .forms import StudentRegistrationForm, StudentProfileForm, UserForm
from .utils import enrolled_only

def index(response):
    return render(response, 'main/base.html', {})

def home(response):
    return render(response, 'main/home.html', {})

def course_list(request):
    courses = CourseTitle.objects.all()
    return render(request, 'main/course_list.html', {'courses':courses})

@enrolled_only
def course_content(request, course_id):
    course = CourseTitle.objects.get(id=course_id)
    return render(request, 'main/course_content.html', {'course':course})

def course_detail(request, course_id):
    course = CourseTitle.objects.get(id=course_id)
    return render(request, 'main/course_detail.html', {'course':course})

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
    enrolments = Enrolment.objects.filter(student=request.user).select_related('course_title')
    return render(request, 'main/profile.html', {'profile': profile, 'enrolments': enrolments})

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
    
def course_enrol(request, course_id):
    course = CourseTitle.objects.get(id=course_id)

    # Check if the user is authenticated
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        # Check if the user is already enrolled in the course
        if Enrolment.objects.filter(student=request.user, course_title=course).exists():
            messages.warning(request, f'You are already enrolled in {course.title}.')
            return redirect('course_content', course_id=course.id)
        else:
            # Create new enrolment
                Enrolment.objects.create(student=request.user, course_title=course)
                messages.success(request, f'You have successfully enrolled in {course.title}.')
                return redirect('course_content', course_id=course.id)
