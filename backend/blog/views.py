from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from .models import Blog
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin # 最基本的權限
from rest_framework.viewsets import ModelViewSet
from .serializers import BlogSerializer


def index(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs':blogs})
    # return HttpResponse("Hello, world. You're at the blog index.")
# Create your views here.

class BlogViewSet(ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

class BlogList(ListView):
    model = Blog
    template_name = 'blogList.html'
    
class BlogCreate(LoginRequiredMixin, CreateView):
    model = Blog
    fields = '__all__'
    template_name = 'form.html'
    
    def get_success_url(self):
        return reverse('BlogList')

class BlogUpdate(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = '__all__'
    template_name = 'form.html'

    def get_success_url(self):
        return reverse('BlogList')