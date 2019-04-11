from django.urls import path
from . import views
from .views import ClassListView, ClassDetailView, ClassCreateView

urlpatterns = [
    path('', ClassListView.as_view(), name='admin-home'),
    path('class/<int:pk>/', ClassDetailView.as_view(), name='class-detail'),
    path('class/new/', ClassCreateView.as_view(), name='class-create'),
    path('students/', views.students, name='admin-students'),
    path('teachers/', views.teachers, name='admin-teachers'),
    path('about/', views.about, name='admin-about'),
]