from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

LEVEL_CHOICES = [
    ('A1', 'Beginner: A1'),
    ('A2', 'Elementary: A2'),
    ('B1', 'Intermediate: B1'),
    ('B2', 'High Intermediate: B2'),
    ('C1', 'Advanced: C1'),
    ('C2', 'Proficient: C2'),
]

class StudentRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=25, required=True)
    last_name = forms.CharField(max_length=25, required=True)
    level = forms.ChoiceField(choices=LEVEL_CHOICES, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'level', 'password1', 'password2']