from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.urls import path,include
from . import views
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
	path('', views.home, name='home'),
	path('tutorials/', views.tutorials, name='tutorials'),
	path('contributions/', views.contributions, name='contributions'),
	path('payments/', views.payments, name='payments'),
	path('login/', auth_views.login, name='login'),
	path('logout/', auth_views.logout, name='logout'),
	path('signup/',views.SignUp.as_view(), name='signup'),
	path('addfoss/', views.AddFoss.as_view(), name='addfoss'),
	path('addtutorial/', views.AddTutorial.as_view(), name='addtut'),
	path('profile/<int:profile_id>/', views.profile, name='profile'),
	path('upload/<int:tutorial_id>/', views.upload, name='upload'),
]

