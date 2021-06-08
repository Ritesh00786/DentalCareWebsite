from django.shortcuts import render
from django.core.mail import send_mail

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
	return render(request, 'about.html', {})

def service(request):
	return render(request, 'service.html', {})

def pricing(request):
	return render(request, 'pricing.html', {})

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

