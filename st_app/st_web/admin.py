#All admin related settings and model registration is done here

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin   				# User admin method to be used 
from .forms import CustomUserCreationForm, CustomUserChangeForm		#importing forms 
from st_web.models import user,foss,tutorial_detail,payment		#importing models 

# User admin class with user creation form and fields to be displayed 

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = user                   # User model is to be worked with
    list_display = ['username', 'email', 'contributions']		# These fields will be displayed in admin panel under user table 


#Registering all the models to be used for in admin panel 

admin.site.register(user, CustomUserAdmin)
admin.site.register(foss)
admin.site.register(tutorial_detail)
admin.site.register(payment)