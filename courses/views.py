from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def courseHome(request):
    allCourses = Course.objects.all()
    
    context = {
        "courses": allCourses
    }

    return render(request,'courses/courseshome.html', context)

def details(request,id):
    course = Course.objects.get(id=id)

    context= {
        "course":course
    }
    return render(request, 'courses/details.html',context)