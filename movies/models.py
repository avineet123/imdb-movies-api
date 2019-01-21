from __future__ import unicode_literals
from decimal import Decimal
from django.db import models

class Genre(models.Model):
    """
    Genre model : Table for movie Genres
    """
    name = models.CharField(max_length=500)

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

    def __str__(self):
        return self.name
    

class Movie(models.Model):
    """
    Movie model : model for Movies
    """
    name = models.CharField(max_length=500)
    imdb_score = models.DecimalField(max_digits=4, decimal_places=1,default=Decimal('0.0'))
    popularity =  models.DecimalField(max_digits=4, decimal_places=1,default=Decimal('0.0'))
    director = models.CharField(max_length=500)
    genre = models.ManyToManyField(Genre)

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return self.name
