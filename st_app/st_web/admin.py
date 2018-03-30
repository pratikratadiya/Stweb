from django.contrib import admin

from st_web.models import user
from st_web.models import foss
from st_web.models import tutorial_detail
from st_web.models import payment
# Register your models here.

admin.site.register(user)
admin.site.register(foss)
admin.site.register(tutorial_detail)
admin.site.register(payment)