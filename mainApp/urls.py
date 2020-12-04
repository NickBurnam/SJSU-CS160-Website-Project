from django.urls import path
from . import views

app_name = "mainApp"

urlpatterns = [
    path('', views.home, name="home"),   
    path('home/', views.home, name="home"), 
    path('not_authorized/', views.not_authorized, name="not_authorized"), 
]
