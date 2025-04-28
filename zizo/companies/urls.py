from django.urls import path
from . import views

app_name = 'companies'

urlpatterns = [
    path('', views.company_list, name='company_list'),
    path('create/', views.create_company, name='create_company'),
    path('<int:company_id>/', views.company_detail, name='company_detail'),
    path('<int:company_id>/update/', views.update_company, name='update_company'),
    path('<int:company_id>/delete/', views.delete_company, name='delete_company'),
    path('<int:pk>/update/', views.update_company, name='update_company'),
]