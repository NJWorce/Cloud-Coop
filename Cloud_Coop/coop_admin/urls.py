from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='coop_admin-home'),
]