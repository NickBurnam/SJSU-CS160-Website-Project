from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db.models import Avg
from django.shortcuts import redirect
from .forms import *

# Create your views here.
def courseHome(request):
    allCourses = Course.objects.all()
    
    context = {
        "courses": allCourses
    }

    return render(request,'courses/courseshome.html', context)

def details(request,id):
    course = Course.objects.get(id=id)
    reviews = Review.objects.filter(course=id)
    context= {
        "course":course,
        "reviews": reviews
    }
    return render(request, 'courses/details.html',context)

def add_review(request, id):
    if request.user.is_authenticated:
        course = Course.objects.get(id=id)
        if request.method == 'POST':
            form = ReviewForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit = False)
                data.comment = request.POST["comment"]
                data.rating = request.POST["rating"]
                data.user = request.user
                data.course = course
                data.save()
                return redirect("courses:detail",id)
            else:
                form.ReviewForm()
            return render(request, 'courses/details.html', {"form",form})
    else:
        return redirect("accounts:login")
