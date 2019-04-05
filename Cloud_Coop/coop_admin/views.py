from django.shortcuts import render
from django.http import HttpResponse
from .models import Class
from django.contrib.auth.models import User


def home(request):
	context = {
	    "classes": Class.objects.all(),
	    "title": "Class View"
	}


	return render(request, 'coop_admin/home.html', context)
	

def about(request):
	return render(request, 'coop_admin/about.html', {'title': 'About Page'})


def students(request):

	context ={
	    "students": User.objects.filter(groups=2),
	    "title": "Students"
	}
	return render(request, 'coop_admin/students.html', context)


def teachers(request):

	context = {
	
		"teachers": User.objects.filter(groups=3),
		"title": "Teachers"
	}
	return render(request, 'coop_admin/teachers.html', context)