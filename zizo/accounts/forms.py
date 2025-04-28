from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, RecruiterProfile, JobSeekerProfile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    user_type = forms.ChoiceField(
        choices=CustomUser.USER_TYPE_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = CustomUser
        fields = ['email', 'user_type', 'password1', 'password2']

class RecruiterProfileForm(forms.ModelForm):
    class Meta:
        model = RecruiterProfile
        fields = ['company', 'position', 'website']

class JobSeekerProfileForm(forms.ModelForm):
    class Meta:
        model = JobSeekerProfile
        fields = ['resume', 'skills', 'experience_years']