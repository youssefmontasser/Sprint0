from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, RequestContext
from app1.models import user

def home(request):
	return render_to_response('home.html', {}, context_instance=RequestContext(request))


def home2(request):
	return render_to_response('homepage2.html', {}, context_instance=RequestContext(request))


def abc(request):

	if request.POST:
		email = request.POST['email']
		username = request.POST['username']
		firstname = request.POST['fn']
		lastname = request.POST['ln']
		password = request.POST['pass']
		confirmpassword = request.POST['cpass'] 
		companyname = request.POST['cname']
		dateoforigin = request.POST['date']

		u = user(user_email=email, user_name=username, first_name=firstname, Last_name=lastname, password=password, confirm_password=confirmpassword, company_name=companyname, company_date_of_origin=dateoforigin)
		u.save()

	return render_to_response('signup.html', {}, context_instance=RequestContext(request))
