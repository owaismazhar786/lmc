# from django.http.response import HttpResponse
from django.shortcuts import render

from blog.models import blogpost

# Create your views here.


def blog(request):
    posts = blogpost.objects.all()
    print(posts)
    return render(request, 'blog/blog.html', {'posts': posts})
