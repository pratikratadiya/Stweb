# urls.py has all the paths to which the mentioned URLs should get redirected to 
from django.contrib import admin
from django.contrib.auth import views as auth_views   # Using auth_views to get Django's authorization views ready!
from django.conf.urls import url
from django.urls import path,include
from . import views                     # Importing views.py file 
from django.conf import settings 

urlpatterns = [
	path('', views.home, name='home'),
	path('tutorials/', views.tutorials, name='tutorials'),  # Look for tutorials in views.py file 
	path('contributions/', views.contributions, name='contributions'),  
	path('payments/', views.payments, name='payments'),
	path('login/', auth_views.login, name='login'),
	path('logout/', auth_views.logout, name='logout'),
	path('signup/',views.SignUp.as_view(), name='signup'),      #Defining SignUp class as a view to display
	path('addfoss/', views.AddFoss.as_view(), name='addfoss'),
	path('addtutorial/', views.AddTutorial.as_view(), name='addtut'),
	path('profile/<int:profile_id>/', views.profile, name='profile'), # Path with profile_id as a parameter
	path('upload/<int:tutorial_id>/', views.upload, name='upload'),
]

