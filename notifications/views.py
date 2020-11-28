from django.shortcuts import render, redirect
from mainApp.models import Page
from django.http import HttpResponse
from .models import *

# Create your views here.

def add_subscription(request, pageId) :

    #return HttpResponse("<h1>Test 1</h1>")

    if request.user.is_authenticated:
        page = Page.objects.get(id=pageId)
        #to do: validate that this retrieved a page?

        sub = 0

        #return HttpResponse("<h1>Test 2</h1>")

        try:
            sub = Subscription.objects.get(page=page, user=request.user)
            return HttpResponse("<h1>You are already subscribed</h1>")
        except Subscription.DoesNotExist:
            sub = Subscription()
            sub.user = request.user
            sub.page = page

            sub.save()
            return HttpResponse("<h1>You have been subscribed to this page!.</h1>")

        #TO DO: check if there's an existing subscription to this page for the current user.

        #TO DO: if not, create a new instance of the class, then save.

        return render(request, 'notifications/add_subscription.html')
    else:
        return HttpResponse("<h1>You need to log in first</h1>")
        return redirect("accounts:login")

def test(request):
    return HttpResponse("<h1>This is a test response</h1>")