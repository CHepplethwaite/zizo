from django.contrib import admin
from django.urls import path
from django.urls import include
from core.views import home

urlpatterns = [
    path('', home, name='home'),
    path('zizo_admin_panel/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('companies/', include('companies.urls')),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
]
