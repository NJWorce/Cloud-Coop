from django.shortcuts import render
from django.http import HttpResponse
from .models import Class
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView


def home(request):
	context = {
	    "classes": Class.objects.all(),
	    "title": "Class View"
	}
	return render(request, 'coop_admin/home.html', context)
	

class ClassListView(ListView):
	model = Class
	template_name = 'coop_admin/home.html'
	context_object_name = 'classes'
	ordering = ['name']

class ClassDetailView(DetailView):
	model = Class

class ClassCreateView(CreateView):

	model = Class
	fields = ['name', 'teacher', 'description']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

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