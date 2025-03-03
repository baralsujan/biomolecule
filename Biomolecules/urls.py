"""Biomolecules URL Configuration

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
from django.contrib.auth import views

from django.conf.urls import url
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('api/v1/', include('DNASequencer.urls')),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^submit/', TemplateView.as_view(template_name='submission.html'), name='submission'),
    url(r'^login/$', views.LoginView.as_view(), {'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), {'template_name': 'registration/logged_out.html'}, name='logout'),]