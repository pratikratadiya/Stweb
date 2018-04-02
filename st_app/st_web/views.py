from django.urls import reverse_lazy
from django.views import generic 
from django import forms
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .forms import CustomUserCreationForm, TutorialAddForm, TutorialUploadForm
import datetime 
from django.shortcuts import render,get_object_or_404,redirect

from .models import tutorial_detail,user,payment,foss

class SignUp(generic.CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'st_web/signup.html'

@method_decorator(staff_member_required, name='dispatch')
class AddFoss(generic.CreateView):
	model = foss
	fields = '__all__'
	success_url = reverse_lazy('home')
	template_name = 'st_web/addfoss.html'

@method_decorator(staff_member_required, name='dispatch')
class AddTutorial(generic.CreateView):
	form_class = TutorialAddForm
	success_url = reverse_lazy('home')
	template_name = 'st_web/addtutorial.html'


def profile(request, profile_id):
	prof = get_object_or_404(user, pk=profile_id)
	pend_list = tutorial_detail.objects.filter(actual_date__isnull=True,parent_foss__contributor__id=profile_id)
	return render(request, 'st_web/profile.html',{'prof':prof,'pend_list':pend_list,})


def upload(request, tutorial_id):
    tutorial = get_object_or_404(tutorial_detail, pk=tutorial_id)
    if request.method == "POST":
        form = TutorialUploadForm(request.POST, request.FILES, instance=tutorial)
        if form.is_valid():
            tutorial = form.save(commit=False)
            tutorial.actual_date = datetime.date.today()
            tutorial.save()
            return redirect('home')
    else:
        form = TutorialUploadForm(instance=tutorial)
    return render(request, 'st_web/upload.html', {'form': form,'tutorial': tutorial,})

a = user.objects.all()

# Create your views here.

def home(request):
	return render(request, 'st_web/index.html',{})

def tutorials(request):
	tut_list = tutorial_detail.objects.filter(actual_date__isnull=False).order_by('-actual_date')
	context = {'tut_list': tut_list}
	return render(request, 'st_web/tutorials.html', context)

def contributions(request):
	for x in a:
		mentions = tutorial_detail.objects.filter(actual_date__isnull=False,parent_foss__contributor=x).count()
		x.contributions = mentions
		x.save()
	con_list = user.objects.order_by('-contributions')
	context = {'con_list': con_list}
	return render(request, 'st_web/contributions.html', context)

def payments(request):
	for x in a:
		exists = payment.objects.filter(user = x)
		if exists.count() == 0:
			add = payment(user = x, amount = x.contributions*1000)
			add.save()
		else:
			existing_user = exists[0]
			existing_user.amount = x.contributions * 1000
			existing_user.save()
	payment_list = payment.objects.order_by('-amount')
	context = {'payment_list': payment_list}
	return render(request, 'st_web/payments.html', context)	