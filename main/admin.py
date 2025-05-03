from django.contrib import admin
from .models import CourseTitle, CourseType, Enrolment #, CourseTitleTypeNexus

admin.site.register(CourseTitle)
admin.site.register(CourseType)
# admin.site.register(CourseTitleTypeNexus)

class EnrolmentAdmin(admin.ModelAdmin):
    enrolment_display=('student', 'course_title', 'enrolment_date')
    enrolment_filter=('student', 'course_title')
    search_by = ('student__username', 'course_title__title')

admin.site.register(Enrolment, EnrolmentAdmin)