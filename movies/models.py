from django.db import models

# Create your models here.
class movies(models.Model):
    imdb_movie_id=models.CharField(max_length=250)
    Title=models.CharField(max_length=250)
    Released = models.CharField(max_length=250)
    Runtime = models.CharField(max_length=250)
    Genre = models.CharField(max_length=250)
    Director = models.CharField(max_length=250)
    Writer = models.CharField(max_length=250)
    story_line = models.CharField(max_length=250) #plot
    Language = models.CharField(max_length=250)
    Country = models.CharField(max_length=250)
    Awards = models.CharField(max_length=250)
    Poster = models.CharField(max_length=250)