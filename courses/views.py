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
    reviews = Review.objects.filter(course=id).order_by("-comment")

    average = reviews.aggregate(Avg("rating"))["rating__avg"]
    if average == None:
        average = 0.0
    average = round(average,2)
    context= {
        "course":course,
        "reviews": reviews,
        "average":average
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
                form = ReviewForm()
            return redirect("courses:detail",id)
    else:
        return redirect("accounts:login")

def edit_review(request, course_id, review_id):
    if request.user.is_authenticated:
        course = Course.objects.get(id=course_id)
        review = Review.objects.get(course = course, id= review_id)

        if request.user == review.user:

            if request.method == "POST":
                form = ReviewForm(request.POST, instance= review)
                if form.is_valid():
                    data = form.save(commit = False)
                    if(data.rating > 10) or (data.rating < 0):
                         error = "Out or range. Please select rating from 0 to 10."
                         return render(request, 'courses/editreview.html', {"error": error, "form": form})
                    else:
                        data.save()
                        return redirect("courses:detail", course_id)
            else:
                form= ReviewForm(instance=review)
            return render(request,'courses/editreview.html',{"form":form})

        else:
            return redirect("courses:detail",course_id)
    else:
        return redirect("accounts:login")

def delete_review(request, course_id, review_id):
    if request.user.is_authenticated:
        course = Course.objects.get(id=course_id)
        review = Review.objects.get(course = course, id= review_id)

        if request.user == review.user:
             review.delete()
        return redirect("courses:detail",course_id)
    else:
        return redirect("accounts:login") 

