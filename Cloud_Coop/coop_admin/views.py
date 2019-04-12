from django.shortcuts import render
from django.http import HttpResponse
from .models import Class
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView,
								  DeleteView)


def home(request):
	context = {
	    "classes": Class.objects.all(),
	    "title": "Class View"
	}
	return render(request, 'coop_admin/home.html', context)
	

class ClassListView(LoginRequiredMixin, ListView):
	model = Class
	template_name = 'coop_admin/home.html'
	context_object_name = 'classes'
	ordering = ['name']

class ClassDetailView(LoginRequiredMixin, DetailView):
	model = Class

class ClassCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):

	model = Class
	fields = ['name', 'teacher', 'description']


	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		return self.request.user.groups.filter(name="Admin").exists()



		
		



class ClassUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

	model = Class
	fields = ['name', 'teacher', 'description']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		class_object = self.get_object()
		if self.request.user == class_object.author or self.request.user.groups.filter(name='Admin'):
			return True
		return False

class ClassDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Class
	success_url = 'coop-admin/loss'

	def test_func(self):
		class_object = self.get_object()
		if self.request.user == class_object.author or self.request.user.groups.filter(name='Admin'):
			return True
		return False

def loss(request):
	return render(request, 'coop_admin/loss.html')

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