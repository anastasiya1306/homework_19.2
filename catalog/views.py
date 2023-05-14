from django.shortcuts import render

def get_home(request):
    return render(request, 'catalog/home.html')

def get_contacts(request):
    return render(request, 'catalog/contacts.html')
