from django.shortcuts import render

# Create your views here.
def blogIndex(request):
     return render(request, 'blog/blogIndex.html')