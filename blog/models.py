from django.db import models
from mainApp.models import Page
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class BlogArticle(Page) :
    date = models.DateField("Post date")
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    image = models.URLField(default=None, null=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('blog:article-detail', args=(str(self.id)) )