from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Page(models.Model) :
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    #body = models.TextField()
    body = RichTextField(blank=True, null=True)
    

    