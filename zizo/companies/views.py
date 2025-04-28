from django.shortcuts import render, redirect, get_object_or_404
from .forms import CompanyForm
from .models import Company
from django.contrib import messages

def create_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save()
            messages.success(request, 'Company created successfully!')
            return redirect('companies:company_detail', pk=company.pk)
    else:
        form = CompanyForm()
    
    return render(request, 'companies/company_form.html', {'form': form})

def company_list(request):
    companies = Company.objects.all()
    return render(request, 'companies/company_list.html', {'companies': companies})

def company_detail(request, pk):
    company = get_object_or_404(Company, pk=pk)
    return render(request, 'companies/company_detail.html', {'company': company})

def update_company(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            messages.success(request, 'Company updated successfully!')
            return redirect('companies:company_detail', pk=company.pk)
    else:
        form = CompanyForm(instance=company)
    
    return render(request, 'companies/company_form.html', {
        'form': form,
        'company': company
    })

# Add this delete view
def delete_company(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        company.delete()
        messages.success(request, 'Company deleted successfully!')
        return redirect('companies:company_list')
    return render(request, 'companies/company_confirm_delete.html', {'company': company})