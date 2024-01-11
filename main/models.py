from django.db import models

# Create your models here.
class Genre(models.Model):
	name = models.CharField(max_length=32)
	description = models.TextField()

	def __str__(self):
		return self.name

class Book(models.Model):
	genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
	name = models.CharField(max_length=128)
	author = models.CharField(max_length=128)
	year = models.IntegerField()
	description = models.TextField()
	link = models.CharField(max_length=512)

	def __str__(self):
		return self.name