from django.contrib import admin
from .models import Company

class CompanyAdmin(admin.ModelAdmin):
    # Define the fields to display in the list view
    list_display = ('name', 'location', 'website', 'industry', 'employee_count', 'established_date')
    
    # Add search functionality for some key fields
    search_fields = ('name', 'location', 'industry', 'contact_email')
    
    # Add filters to make it easier to filter records based on certain criteria
    list_filter = ('industry', 'employee_count', 'established_date')
    
    # Allow ordering by certain fields
    ordering = ('-established_date',)
    
    # Add form layout for the detail page
    fieldsets = (
        (None, {'fields': ('name', 'description', 'location', 'website', 'logo')}),
        ('Contact Information', {'fields': ('contact_email', 'contact_phone', 'social_media_links')}),
        ('Company Details', {'fields': ('established_date', 'employee_count', 'industry')}),
    )
    
    # Make sure to add the inline to the list if needed
    # inlines = [YourInlineModelAdmin]

# Register the model and custom admin
admin.site.register(Company, CompanyAdmin)
