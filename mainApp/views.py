from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'mainApp/index.html', {})

def not_authorized(request):
    return render(request, 'mainApp/not_authorized.html', {})