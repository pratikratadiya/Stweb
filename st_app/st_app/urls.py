"""st_app URL Configuration

The `urlpatterns` list routes URLs to views.

"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),        # Including admin URLs 
    path('', include('st_web.urls')),       # Redirecting all links to urls.py file of st_web app 
]
