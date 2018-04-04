# All forms used in the app are stored here

from django import forms
from django.core.exceptions import ValidationError                          # Validation Error method 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm      # Using django's predefined forms
from .models import user, tutorial_detail
import datetime 

# Form for creating new user 
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = user                                        # using the user model
        fields = ('username', 'email', 'name')
        help_texts = {'username':(''), 'email':(''), 'name':(''),}

# Form to change information of existing user    	    	
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = user
        fields = UserChangeForm.Meta.fields

# Form for adding/assigning a new tutorial(for admin)
class TutorialAddForm(forms.ModelForm):

	class Meta:
		model = tutorial_detail
		fields = ('parent_foss', 'tutorial_name', 'expected_date', )        # Fields to be part of the form
		help_texts = { 'expected_date': ('Enter in the format YYYY-MM-DD'), }   # Help Text to be displayed


# Form for uploading tutorial(for contributors)
class TutorialUploadForm(forms.ModelForm):

	class Meta:
		model = tutorial_detail
		fields = ('tutorial',)      # Only File field will be a part of the form 
		
