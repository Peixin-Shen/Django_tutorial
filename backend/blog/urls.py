"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index, BlogViewSet, BlogList, BlogCreate, BlogUpdate
from django.contrib.auth.views import LoginView, LogoutView

router = DefaultRouter()
router.register('blog', BlogViewSet)

urlpatterns = [
    path('', index, name='Index'),
    path('login/', LoginView.as_view(template_name='form.html'), name='Login'),
    path('logout/', LogoutView.as_view(), name='Logout'),
    path('blog/', BlogList.as_view(), name='BlogList'),
    path('blog/create/', BlogCreate.as_view(), name='BlogCreate'),
    path('blog/update/<pk>/', BlogUpdate.as_view(), name='BlogUpdate'),
    path('api/', include(router.urls)),
]