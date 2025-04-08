from django.db import models
from django.contrib.auth.models import User

class CourseTitle(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    details = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    beginners = models.BooleanField()
    # relationship between coursetitle and coursetype via the nexus model
    course_types = models.ManyToManyField('CourseType', through='CourseTitleTypeNexus')

    def __str__(self):
        return self.title
    
class CourseType(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    details = models.TextField()
    # relationship between coursetitle and coursetype via the nexus model
    course_titles = models.ManyToManyField('CourseTitle', through='CourseTitleTypeNexus')

    def __str__(self):
        return self.name
    
class CourseTitleTypeNexus(models.Model):
    course_title = models.ForeignKey(CourseTitle, on_delete=models.CASCADE)
    course_type = models.ForeignKey(CourseType, on_delete=models.CASCADE)

class Enrolment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course_title = models.ForeignKey('CourseTitle', on_delete=models.CASCADE)
    enrolment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student.username} enrolled in {self.course_title.title}'

