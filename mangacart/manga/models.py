from django.db import models

# Create your models here.
class Mangacard(models.Model):
    isbn = models.CharField(max_length=255, unique=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year_of_publication = models.IntegerField(default=0)
    publisher = models.CharField(max_length=255)
    image_url = models.URLField(max_length=200)