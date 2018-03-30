from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.urls import path,include
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('tutorials/', views.tutorials, name='tutorials'),
	path('contributions/', views.contributions, name='contributions'),
	path('payments/', views.payments, name='payments'),
	path('login/', auth_views.login, name='login'),
	path('logout/', auth_views.logout, name='logout'),
]