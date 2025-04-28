from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    website = models.URLField(blank=True)
    logo = models.ImageField(upload_to='company_logos/', blank=True)
    established_date = models.DateField(null=True, blank=True)
    employee_count = models.PositiveIntegerField(null=True, blank=True)
    industry = models.CharField(max_length=100, blank=True)
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    social_media_links = models.JSONField(blank=True, null=True)