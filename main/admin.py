from django.contrib import admin
from .models import CourseTitle, CourseType, Enrolment #, CourseTitleTypeNexus

admin.site.register(CourseTitle)
admin.site.register(CourseType)
# admin.site.register(CourseTitleTypeNexus)

class EnrolmentAdmin(admin.ModelAdmin):
    list_display=('course_title','student',  'enrolment_date')
    list_filter=('student', 'course_title')
    search_fields = ('student__username', 'course_title__title')

admin.site.register(Enrolment, EnrolmentAdmin)