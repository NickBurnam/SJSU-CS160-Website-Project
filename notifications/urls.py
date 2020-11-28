from django.urls import path
from . import views

app_name = "notifications"

urlpatterns = [
    path('add_subscription/<int:pageId>/', views.add_subscription, name="add_subscription"),
    path('notify_subscribers/<int:pageId>/', views.notify_subscribers, name="notify_subscribers"),
    path('', views.test, name="test"),
]
