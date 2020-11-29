from django.shortcuts import render, redirect
from mainApp.models import Page
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import *
import os

# Create your views here.

def view_subscriptions(request):

    if request.user.is_authenticated:
        subs = Subscription.objects.all().filter(user=request.user)

        return render(request, 'notifications/view_subscriptions.html', {'subscriptions': subs})
    else:
        return redirect("accounts:login")

def add_subscription(request, pageId) :

    if request.user.is_authenticated:
        page = Page.objects.get(id=pageId)
        
        try:
            pass
        except:
            pass

        try:
            sub = Subscription.objects.get(page=page, user=request.user)
            #user is already subscribed, nothing to do
        except Subscription.DoesNotExist:
            sub = Subscription()
            sub.user = request.user
            sub.page = page
            sub.save()
        return redirect("notifications:view_subscriptions")
    else:
        return redirect("accounts:login")

def delete_subscription(request, subId):
    
    if request.user.is_authenticated:
        
        try:
            sub = Subscription.objects.get(id=subId, user=request.user)

            if sub.user == request.user:
                sub.delete()
                return redirect("notifications:view_subscriptions")
            else:
                return redirect("mainApp:not_authorized")

        except Subscription.DoesNotExist:
            return redirect("mainApp:not_authorized")
    else:
        return redirect("accounts:login")

def notify_subscribers(request, pageId) :

    if not request.user.is_staff:
        return redirect("mainApp:not_authorized")
    
    subs = Subscription.objects.filter(id=pageId)

    for curSub in Subscription.objects.filter(page_id=pageId):
        curSubUser = User.objects.get(id=curSub.user_id)
        
        if(curSubUser.email != ''):
            print("sending email to: " + curSubUser.email)

            #uncomment this when ready
            #TODO use an HTML template for the email body?

            # send_mail(
            #     'Subscribed Article has been updated',
            #     'This is a test notification',
            #     'team1admin@someDomain.com',
            #     [curSubUser.email],
            #     fail_silently=False
            # )
        

    return render(request, 'notifications/notifications_sent.html')


