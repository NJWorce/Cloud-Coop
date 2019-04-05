from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Class(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	date_created = models.DateTimeField(default=timezone.now)

	teacher = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    
	def __str__(self):
		return self.name

