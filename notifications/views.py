from django.shortcuts import render, redirect
from mainApp.models import Page
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import *
import os

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


def notify_subscribers(request, pageId) :

    #TO DO: check that request is from a staff user
    
    subs = Subscription.objects.filter(id=pageId)

    for curSub in Subscription.objects.filter(page_id=pageId):
        curSubUser = User.objects.get(id=curSub.user_id)
        
        if(curSubUser.email != ''):
            print("sending email to: " + curSubUser.email)

            print(os.environ.get('DB_USER') )

            # send_mail(
            #     'Subscribed Article has been updated',
            #     'This is a test notification',
            #     'team1admin@someDomain.com',
            #     [curSubUser.email],
            #     fail_silently=False
            # )
        

    return HttpResponse("<h1>Notifying subscribers...</h1>")

def test(request):
    return HttpResponse("<h1>This is a test response</h1>")

