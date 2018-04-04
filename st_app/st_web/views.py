# All views for the URLs are defined here

from django.urls import reverse_lazy        # Lazy implementation of the reverse URL resolver 
from django.views import generic            # Generic views 
from django import forms
from django.contrib.admin.views.decorators import staff_member_required     # Views accessoble to only admin
from django.utils.decorators import method_decorator
from .forms import CustomUserCreationForm, TutorialAddForm, TutorialUploadForm  # Importing forms defined by us
import datetime 
from django.shortcuts import render,get_object_or_404,redirect      # Rendering and redirecting utilities 

from .models import tutorial_detail,user,payment,foss

# Signup class using CreateView of generic views 
class SignUp(generic.CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')     # Redirect to home page on successful registration
	template_name = 'st_web/signup.html'

# Add foss class with a method decorator which allows only admin to access this view 
@method_decorator(staff_member_required, name='dispatch')
class AddFoss(generic.CreateView):
	model = foss                        # Form for the model FOSS 
	fields = '__all__'
	success_url = reverse_lazy('home')
	template_name = 'st_web/addfoss.html'

# Add tutorial class with a method decorator which allows only admin to access this view 
@method_decorator(staff_member_required, name='dispatch')
class AddTutorial(generic.CreateView):
	form_class = TutorialAddForm
	success_url = reverse_lazy('home')
	template_name = 'st_web/addtutorial.html'

# Profile page view 
def profile(request, profile_id):
    # Will search for user object having ID as that requested, if found will continue else show 404 error 
	prof = get_object_or_404(user, pk=profile_id)   
	# List tutorials who don't have actual date i.e. aren't submitted and contributor id is that requested 
	pend_list = tutorial_detail.objects.filter(actual_date__isnull=True,parent_foss__contributor__id=profile_id)
	return render(request, 'st_web/profile.html',{'prof':prof,'pend_list':pend_list,})

# View to upload form 
def upload(request, tutorial_id):
    tutorial = get_object_or_404(tutorial_detail, pk=tutorial_id)   # Get tutorial object with pk requested 
    if request.method == "POST":        # If data has been posted 
        form = TutorialUploadForm(request.POST, request.FILES, instance=tutorial)
        if form.is_valid():                         # If data in the form is valid  
            tutorial = form.save(commit=False)      # Don't save the form immediately 
            tutorial.actual_date = datetime.date.today()    # Add today's date as the actual_date and save 
            tutorial.save()     
            return redirect('home')                 # Redirect to home 
    else:       # If form is accessed for the first time 
        form = TutorialUploadForm(instance=tutorial)
    return render(request, 'st_web/upload.html', {'form': form,'tutorial': tutorial,})

a = user.objects.all()  

# Return home page 
def home(request):
	return render(request, 'st_web/index.html',{})

# Return list of contributed tutorials 
def tutorials(request):
# Filter out objects having actual date i.e. already submitted and order by most recent 
	tut_list = tutorial_detail.objects.filter(actual_date__isnull=False).order_by('-actual_date')
	context = {'tut_list': tut_list}
	return render(request, 'st_web/tutorials.html', context)

# Return contributions per contributor in a month 
def contributions(request):
# For every contributor in the user table 
	for x in a:             
# FInd the count of objects who (have been submitted AND whose contributor is x )
		mentions = tutorial_detail.objects.filter(actual_date__isnull=False,parent_foss__contributor=x).count()
		x.contributions = mentions      # Mark the count as contributions of x and save 
		x.save()
# Make list of users in descending order of contributions and send it to the template (excluding admin)
	con_list = user.objects.exclude(is_superuser=True).order_by('-contributions')
	context = {'con_list': con_list}
	return render(request, 'st_web/contributions.html', context)

# Return amount payable per contributor 
def payments(request):
	for x in a:
		exists = payment.objects.filter(user = x)   # Check if there already exists an instance of x 
		if exists.count() == 0:                     # If no, create a new instance and save 
			add = payment(user = x, amount = x.contributions*1000)
			add.save()
		else:
            # If it does exist, multiply contributions by 1000 and save as its amount 
			existing_user = exists[0]               
			existing_user.amount = x.contributions * 1000
			existing_user.save()
    # Send all objects of payment in descending order of amount payable (excluding admin)
	payment_list = payment.objects.exclude(user__is_superuser=True).order_by('-amount')
	context = {'payment_list': payment_list}
	return render(request, 'st_web/payments.html', context)	
