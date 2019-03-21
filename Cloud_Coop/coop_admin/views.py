from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, 'coop_admin/home.html', {'title': 'Class View'})
	

def about(request):
	return render(request, 'coop_admin/about.html', {'title': 'About Page'})


def students(request):
	return render(request, 'coop_admin/students.html', {'title': 'Students'})


def teachers(request):
	return render(request, 'coop_admin/teachers.html', {'title': 'Teachers'})