from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='admin-home'),
    path('students/', views.students, name='admin-students'),
    path('teachers/', views.teachers, name='admin-teachers'),
    path('about/', views.about, name='admin-about'),
]