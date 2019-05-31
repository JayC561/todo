from django.db import models

# Create your models here.
class Task(models.Model):
	title = models.CharField(max_length=64)
	check = models.BooleanField(default=False)
	date_to_do = models.DateField(default='2019-05-26', null=True, blank=True)
	timestamp = models.DateTimeField(auto_now=True, null=True, blank=True)