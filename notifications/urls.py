from django.urls import path
from . import views

app_name = "notifications"

urlpatterns = [
    path('add_subscription/<int:pageId>/', views.add_subscription, name="add_subscription"),
    path('', views.test, name="test"),
]
