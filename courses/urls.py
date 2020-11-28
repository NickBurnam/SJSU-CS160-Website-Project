from django.urls import path, include
from . import views

app_name = "courses"

urlpatterns = [
    path('',views.courseHome,name="courses_home"), 
    path('details/<int:id>/',views.details,name="detail")
]