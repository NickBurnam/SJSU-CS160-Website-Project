from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import BlogArticle
from django.urls import reverse_lazy

# Create your views here.
# def blogIndex(request):
#     return render(request, 'blogIndex.html')


class BlogView(ListView):
    model = BlogArticle
    template_name = "blog/blogIndex.html"
    ordering = ["-date"]

class BlogPostView(DetailView):
    model = BlogArticle
    template_name = "blog/blogPost.html"


class AddBlogPostView(CreateView):
    model = BlogArticle
    template_name = "blog/addBlogPost.html"
    fields = "__all__"


class EditPostView(UpdateView):
    model = BlogArticle
    template_name = "blog/editBlogPost.html"
    fields = "__all__"


class DeletePostView(DeleteView):
    model = BlogArticle
    template_name = "blog/deleteBlogPost.html"
    success_url = reverse_lazy("blog:blog")


def CategoryView(request, cat, sort):
    category_post = BlogArticle.objects.filter(category=cat).order_by(sort)
    return render(
        request, "blog/categories.html", {"cat": cat, "category_post": category_post, "sort": sort}
    )
