from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, RecruiterProfile, JobSeekerProfile

# Register CustomUser with a custom admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'username', 'user_type', 'is_staff', 'is_active')
    list_filter = ('user_type', 'is_staff', 'is_active')
    search_fields = ('email', 'username')
    ordering = ('email',)
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number', 'profile_picture')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_type')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_type')}),
    )
    
    # You can customize the forms if needed
    # form = CustomUserChangeForm
    # add_form = CustomUserCreationForm

# Register RecruiterProfile
class RecruiterProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'position', 'website')
    search_fields = ('user__email', 'company__name', 'position')

# Register JobSeekerProfile
class JobSeekerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'resume', 'skills', 'experience_years')
    search_fields = ('user__email', 'skills')

# Register the models to admin site
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(RecruiterProfile, RecruiterProfileAdmin)
admin.site.register(JobSeekerProfile, JobSeekerProfileAdmin)
