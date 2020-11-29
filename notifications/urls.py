from django.urls import path
from . import views

app_name = "notifications"

urlpatterns = [
    path('add_subscription/<int:pageId>/', views.add_subscription, name="add_subscription"),
    path('delete_subscription/<int:subId>/', views.delete_subscription, name="delete_subscription"),
    path('notify_subscribers/<int:pageId>/', views.notify_subscribers, name="notify_subscribers"),
    path('view_subscriptions/', views.view_subscriptions, name="view_subscriptions"),
    
]
