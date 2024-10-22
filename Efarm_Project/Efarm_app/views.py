from django.shortcuts import render


# Create your views here.
from django.shortcuts import render, HttpResponse
def home(request):
    return render(request, 'home-page.html')

def products(request):
    return render(request, 'products-page.html')

def contact(request):
    return render(request, 'contact-page.html')

def about(request):
    return render(request, 'about-page.html')

def market(request):
    return render(request, 'market-page.html')

def services(request):
    return render(request, 'services-page.html')

def profile(request):
    return render(request, 'profile-page.html')

