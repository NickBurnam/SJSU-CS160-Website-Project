from django.db import models
from mainApp.models import Page

# Create your models here.

class BlogArticle(Page) :
    date = models.DateField("Post date")