from django.contrib import admin
from .models import CourseTitle, CourseType #, CourseTitleTypeNexus, Enrolment

admin.site.register(CourseTitle)
admin.site.register(CourseType)
# admin.site.register(CourseTitleTypeNexus)
# admin.site.register(Enrolment)
