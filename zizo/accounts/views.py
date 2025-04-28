from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import UserRegistrationForm, RecruiterProfileForm, JobSeekerProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = None
        
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            
            # Assuming user_type is part of the form or logic
            new_user.user_type = request.POST.get('user_type', 'job_seeker')  # Default to job_seeker
            new_user.save()

            if new_user.user_type == 'recruiter':
                profile_form = RecruiterProfileForm(request.POST, request.FILES)
            else:
                profile_form = JobSeekerProfileForm(request.POST, request.FILES)
            
            if profile_form and profile_form.is_valid():
                profile = profile_form.save(commit=False)
                profile.user = new_user
                profile.save()
                login(request, new_user)
                messages.success(request, 'Registration successful!')
                return redirect('dashboard') 
        
        # If forms are invalid, re-render with errors
        return render(request, 'accounts/register.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })
    
    else:
        user_form = UserRegistrationForm()
        return render(request, 'accounts/register.html', {
            'user_form': user_form,
            'profile_form': None
        })

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = get_user_model().objects.get(email=email)
            if user.check_password(password):
                login(request, user)
                messages.success(request, f'Welcome back, {user.email}!')
                return redirect('/dashboard/')
            else:
                messages.error(request, 'Invalid password')
        except get_user_model().DoesNotExist:
            messages.error(request, 'Invalid email or password')
    
    return render(request, 'accounts/login.html')

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')

@login_required
def profile(request):
    user = request.user
    if user.user_type == 'recruiter':
        profile = user.recruiterprofile
    elif user.user_type == 'job_seeker':
        profile = user.jobseekerprofile
    else:
        profile = None
    return render(request, 'accounts/profile.html', {'profile': profile})
