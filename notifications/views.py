from django.shortcuts import render, redirect
from mainApp.models import Page
from django.http import HttpResponse

from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

from django.urls import reverse

from .models import *


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

            plainTemplate = get_template('notifications/email_notification.txt')
            htmlTemplate = get_template('notifications/email_notification.html')


            subject = 'Subscribed page has been updated'
            from_email = 'webdevwithdjango@gmail.com'
            to = [curSubUser.email]


            #I'm assuming that only blog articles are getting subscriptions with the pageURL handling.
            context = { 
                'title': curSub.page.title,
                'pageURL':  request.build_absolute_uri(reverse('blog:article-detail', args=[curSub.page.id]) )
            }
            plainContent = plainTemplate.render(context)
            htmlContent = htmlTemplate.render(context)

            #print(plainContent)

            msg = EmailMultiAlternatives(subject, plainContent, from_email, to)
            msg.attach_alternative(htmlContent, "text/html")
            msg.send()


    return redirect("notifications:notify_result")

def notify_result(request):
    return render(request, 'notifications/notifications_sent.html')

