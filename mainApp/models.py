from django.db import models

# Create your models here.

class Page(models.Model) :
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    body = models.TextField()
    

    