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
    path("login/", auth_views.LoginView.as_view(template_name='main/login.html'), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page='home'), name="logout"),
    path('profile/', views.student_profile, name='student_profile'),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
    path("profile/delete/", views.delete_profile, name="delete_profile"),
    path('enrol/<int:course_id>/', views.course_enrol, name='enrol'),
]