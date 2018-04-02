from django.db import models
from django.contrib.auth.models import AbstractUser
from .validator import validate_file_extension, validate_date
# Create your models here.

class user(AbstractUser):
	name = models.CharField(max_length=100)
	contributions = models.IntegerField(default=0)

	def __str__(self):
			return self.name
	
	class Meta:
		verbose_name="user"
		verbose_name_plural="user"


class foss(models.Model):
	contributor = models.OneToOneField(user, on_delete=models.CASCADE)
	foss_name = models.CharField(max_length=100)

	def __str__(self):
		return self.foss_name
	
	class Meta:
		verbose_name="foss"
		verbose_name_plural="foss"

	

class tutorial_detail(models.Model):
	parent_foss = models.ForeignKey(foss, on_delete=models.CASCADE)
	tutorial_name = models.CharField(max_length=150)
	tutorial = models.FileField(upload_to='documents/', validators=[validate_file_extension])
	expected_date = models.DateField(auto_now=False,auto_now_add=False, validators=[validate_date])
	actual_date = models.DateField(auto_now=False,auto_now_add=False,blank=True,null=True)
		
	def __str__(self):
		return self.parent_foss.foss_name + ":" + self.tutorial_name
	
	class Meta:
		verbose_name="tutorial_detail"
		verbose_name_plural="tutorial_detail"
	

class payment(models.Model):
	user = models.ForeignKey(user, on_delete=models.CASCADE)
	amount = models.IntegerField(default=0)
	
	def __str__(self):
			return self.user.name
	
	class Meta:
		verbose_name="payment"
		verbose_name_plural="payment"	