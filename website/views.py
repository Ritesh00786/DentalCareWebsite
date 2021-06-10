from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from django.core import serializers
# import requests


def home(request):
	return render(request, 'home.html', {})

def contact(request):
	
	if request.method == "POST":

		user_name = request.POST['user-name']
		user_email = request.POST['user-email']
		message = request.POST['message']

		#send an email
		send_mail(
				user_name, #subject
				message, #message
				user_email, #from email
				['riteshpoojary190895@gmail.com'] #to email
			)

		return render(request, 'contact.html', { 'user_name' : user_name })

	else:
		return render(request, 'contact.html', {})

def about(request):
	# response = requests.get('http://fakeapi.jsonparseronline.com/users').json()
	# return render(request, 'about.html', {'response' : response})
	return render(request, 'about.html', {})

def service(request):
	return render(request, 'service.html', {})

def pricing(request):
	data = [
	{
		"services" : "Teeth Whitening Service at Dental Clinic",
		"sittings" : "1 times",
		"cost" : "$120.00"
	},
	{
		"services" : "Teeth Whitening Service at home",
		"sittings" : "1 times",
		"cost" : "$110.00"
	},
	{
		"services" : "Ceramic crowns and fillings Dental porcelain",
		"sittings" : "1 times",
		"cost" : "$100.00"
	},
	{
		"services" : "Covering the recession of the gums",
		"sittings" : "1 times",
		"cost" : "$450.00"
	},
	{
		"services" : "Teeth Whitening Service at Dental Clinic",
		"sittings" : "1 times",
		"cost" : "$120.00"
	},
	{
		"services" : "Consultation, impressions and preparation of models",
		"sittings" : "1 times",
		"cost" : "$45.00"
	},
	{
		"services" : "Remove crowns, bridges Service",
		"sittings" : "1 tooth",
		"cost" : "$60.00"
	},
	{
		"services" : "Removal of an old inlay, old crown",
		"sittings" : "1 times",
		"cost" : "$100.00"
	},
	{
		"services" : "Implantation of an implant (price depends on system used)",
		"sittings" : "1 tooth",
		"cost" : "$550.00"
	},
	{
		"services" : "Standard porcelain and zirconium crown on implant",
		"sittings" : "1 tooth",
		"cost" : "$500.00"
	},
	{
		"services" : "Overlay teeth whitening ( 2 arches)",
		"sittings" : "1 times",
		"cost" : "$150.00"
	}
	]
	return render(request, 'pricing.html', {'response' : data})

def appointment(request):
	if request.method == "POST":

		user_name = request.POST['user-name']
		user_phone = request.POST['user-phone']
		user_email = request.POST['user-email']
		user_address = request.POST['user-address']
		user_schedule = request.POST['user-schedule']
		user_date = request.POST['user-date']
		user_message = request.POST['user-message']
		
		#send an email
		send_mail(
				user_name, #subject
				user_message, #message
				user_email, #from email
				['riteshpoojary190895@gmail.com'] #to email
			)
	
		return render(request, 'appointment.html', 
			{ 
			'user_name' : user_name,
			'user_phone' : user_phone,
			'user_email' : user_email,
			'user_address' : user_address,
			'user_schedule' : user_schedule,
			'user_date' : user_date,
			'user_message' : user_message
			})

	else:
		return render(request, 'home.html', {})
