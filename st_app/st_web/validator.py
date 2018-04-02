def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp4', '.mkv', '.flv', '.mpeg', '.wmv', '.3gp']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')

def validate_date(value):
	from django.core.exceptions import ValidationError
	import datetime
	if value and value < datetime.date.today():
		raise ValidationError(u'Invalid Date entered')
