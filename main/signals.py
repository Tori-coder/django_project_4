from allauth.account.signals import user_logged_in
from allauth.socialaccount.signals import user_logged_up
from django.dispatch import receiver
from .models import StudentProfile

@receiver(user_logged_in)
def create_student_profile(sender, request, user, **kwargs):
    if not hasattr(user, 'studentprofile'):
        StudentProfile.objects.create(user=user, level='A1')

@receiver(user_logged_up)
def create_student_profile(sender, request, user, **kwargs):
    if not hasattr(user, 'studentprofile'):
        StudentProfile.objects.create(user=user, level='A1')