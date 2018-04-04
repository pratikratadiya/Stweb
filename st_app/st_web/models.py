from django.db import models
from django.contrib.auth.models import AbstractUser             # Using AbstractUser method to extend user models
from .validator import validate_file_extension, validate_date   # Importing validators written in .validators.py


# user class for our app extending Django's user model with two fields- name and contributions
class user(AbstractUser):
	name = models.CharField(max_length=100)
	contributions = models.IntegerField(default=0)

	def __str__(self):          # Self defining function
			return self.name
	
	class Meta:
		verbose_name="user"
		verbose_name_plural="user"


# foss model having one to one connection with the user class (1 user assigned 1 FOSS)
class foss(models.Model):
	contributor = models.OneToOneField(user, on_delete=models.CASCADE)
	foss_name = models.CharField(max_length=100)

	def __str__(self):
		return self.foss_name
	
	class Meta:
		verbose_name="foss"
		verbose_name_plural="foss"

	
# tutorial_detail model which has a many to one relationship with foss table (1 FOSS has 10 tutorials)
class tutorial_detail(models.Model):
	parent_foss = models.ForeignKey(foss, on_delete=models.CASCADE)
	tutorial_name = models.CharField(max_length=150)
	# Files get uploaded to /media/documents after it is validated
	tutorial = models.FileField(upload_to='documents/', validators=[validate_file_extension])
	# Validator used to validate the expected date 
	expected_date = models.DateField(auto_now=False,auto_now_add=False, validators=[validate_date])
	actual_date = models.DateField(auto_now=False,auto_now_add=False,blank=True,null=True)
		
	def __str__(self):
		return self.parent_foss.foss_name + ":" + self.tutorial_name
	
	class Meta:
		verbose_name="tutorial_detail"
		verbose_name_plural="tutorial_detail"
	

# Payment model which has a foreign key with the user model 
class payment(models.Model):
	user = models.ForeignKey(user, on_delete=models.CASCADE)
	amount = models.IntegerField(default=0)
	
	def __str__(self):
			return self.user.name
	
	class Meta:
		verbose_name="payment"
		verbose_name_plural="payment"	
