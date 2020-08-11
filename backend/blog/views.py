#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog


def index(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs':blogs})
    # return HttpResponse("Hello, world. You're at the blog index.")
# Create your views here.
