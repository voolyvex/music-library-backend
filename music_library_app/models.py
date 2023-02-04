from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=99)
    artist = models.CharField(max_length=99)
    album = models.CharField(max_length=99)
    release_date = models.DateField()
    genre = models.CharField(max_length=99)