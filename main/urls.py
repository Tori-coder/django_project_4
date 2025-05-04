from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("course_list/", views.course_list, name="course_list"),
    path("course_detail/<int:course_id>", views.course_detail, name="course_detail"),
    path("course_content/<int:course_id>", views.course_content, name="course_content"),
    path("register/", views.register, name="register"),
    path('profile/', views.student_profile, name='student_profile'),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
    path("profile/delete/", views.delete_profile, name="delete_profile"),
    path('enrol/<int:course_id>/', views.course_enrol, name='enrol'),
]