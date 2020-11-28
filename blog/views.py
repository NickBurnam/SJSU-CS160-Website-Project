from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogArticle

# Create your views here.
#def blogIndex(request):
#     return render(request, 'blogIndex.html')

class BlogView(ListView):
     model = BlogArticle
     template_name = 'blog/blogIndex.html'

class BlogPostView(DetailView):
     model = BlogArticle
     template_name = 'blog/blogPost.html'