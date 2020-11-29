from django import forms
from .models import *

#course add form
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name','creator','description','last_updated_date','average_rating','image')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("comment","rating")