from django.shortcuts import render

from .models import tutorial_detail,user,payment

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