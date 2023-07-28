from django.db import models

# Create your models here.
class Song(models.Model):
	name=models.CharField(max_length=50,null=True)
	link=models.URLField(max_length=500,null=True)

	def __str__(self):
		return self.name

class songSuggestons(models.Model):
	name=models.CharField(max_length=50,null=True)

	def __str__(self):
		return self.name
