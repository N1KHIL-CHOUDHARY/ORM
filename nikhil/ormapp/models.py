from django.db import models
from django.contrib import admin

class Movie(models.Model):
    MovieName = models.CharField(max_length=100)
    Rating = models.FloatField()
    ReleaseDate = models.DateField()
    Genre = models.CharField(max_length=50)

    def __str__(self):
        return self.MovieName

class MovieAdmin(admin.ModelAdmin):
    list_display = ('MovieName', 'Rating', 'ReleaseDate', 'Genre')
