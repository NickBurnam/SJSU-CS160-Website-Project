from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from mainApp.models import Page

# Create your models here.

class BlogArticle(Page) :
    categories = (
        ('Django tutorial', 'Django tutorial'),
        ('News', 'News'),
        ('Miscellaneous', 'Miscellaneous'),
    )
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    image = models.URLField(default=None, null=True)
    category = models.CharField(max_length=200, default='Miscellaneous', choices=categories)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('blog:blog')