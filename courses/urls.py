from django.urls import path, include
from . import views

app_name = "courses"

urlpatterns = [
    path('',views.courseHome,name="courses_home"), 
    path('details/<int:id>/',views.details,name="detail"),
    path('addreview/<int:id>/',views.add_review,name="add_review"),
    path('editreview/<int:course_id>/<int:review_id>/',views.edit_review,name="edit_review"),
    path('deletereview/<int:course_id>/<int:review_id>/',views.delete_review,name="delete_review")
]