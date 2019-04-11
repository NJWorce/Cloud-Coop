from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Class(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	date_created = models.DateTimeField(default=timezone.now)

	teacher = models.ForeignKey(User, models.SET_NULL, related_name='teacher', blank=True, null=True)
	author = models.ForeignKey(User, models.SET_NULL, related_name='author', blank=True, null=True )

    
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('class-detail', kwargs={'pk': self.pk})

