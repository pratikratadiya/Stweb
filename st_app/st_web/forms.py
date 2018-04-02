from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import user, tutorial_detail
import datetime 

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = user
        fields = ('username', 'email', 'name')
        help_texts = {'username':(''), 'email':(''), 'name':(''),}

    	    	
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = user
        fields = UserChangeForm.Meta.fields

class TutorialAddForm(forms.ModelForm):

	class Meta:
		model = tutorial_detail
		fields = ('parent_foss', 'tutorial_name', 'expected_date', )
		help_texts = { 'expected_date': ('Enter in the format YYYY-MM-DD'), }


class TutorialUploadForm(forms.ModelForm):

	class Meta:
		model = tutorial_detail
		fields = ('tutorial',)
		