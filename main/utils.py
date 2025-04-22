from functools import wraps
from django.shortcuts import redirect, render
from .models import CourseTitle, Enrolment

def enrolled_only(content_view):
    def wrapper(request, course_id):
        course = CourseTitle.objects.get(id=course_id)
        if request.user.is_authenticated:
            if Enrolment.objects.filter(student=request.user, course_title=course).exists()==True:
                return content_view(request, course_id)
            else:
                return render(request, 'main/course_detail.html', {'course':course}) # redirects back to course detail for now. set an error message later
        else:
            return redirect('login')
    return wrapper