from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from st_web.models import user
from st_web.models import foss
from st_web.models import tutorial_detail
from st_web.models import payment
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = user
    list_display = ['username', 'email', 'contributions']

admin.site.register(user, CustomUserAdmin)
admin.site.register(foss)
admin.site.register(tutorial_detail)
admin.site.register(payment)