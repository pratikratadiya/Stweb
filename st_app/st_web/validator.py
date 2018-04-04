# Validators used in models.py for validating fields are written here 

# Function to validate file extension of tutorial file 
def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp4', '.mkv', '.flv', '.mpeg', '.wmv', '.3gp']    # Allowing only valid video formats
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'SPAM detected. Not a video')

# Function to see if valid expected_date is entered
def validate_date(value):
	from django.core.exceptions import ValidationError
	import datetime
	if value and value < datetime.date.today():         # If expected date is from the past raise error
		raise ValidationError(u'Invalid Date entered')
