from django.db import models
from django.contrib.auth.models import User

LEVEL_CHOICES = [
    ('A1', 'Beginner: A1'),
    ('A2', 'Elementary: A2'),
    ('B1', 'Intermediate: B1'),
    ('B2', 'High Intermediate: B2'),
    ('C1', 'Advanced: C1'),
    ('C2', 'Proficient: C2'),
]

class CourseTitle(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    details = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
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
    # course_titles = models.ManyToManyField('CourseTitle', through='CourseTitleTypeNexus')

    def __str__(self):
        return self.name
    
class CourseTitleTypeNexus(models.Model):
    course_title = models.ForeignKey(CourseTitle, on_delete=models.CASCADE)
    course_type = models.ForeignKey(CourseType, on_delete=models.CASCADE)

# create student profile model to add fields to standard django user model
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level = models.CharField(choices=LEVEL_CHOICES)

    def __str__(self):
        return self.user.username

class Enrolment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course_title = models.ForeignKey('CourseTitle', on_delete=models.CASCADE)
    enrolment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student.username} enrolled in {self.course_title.title}'

