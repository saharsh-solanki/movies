import requests
import http.client
import json
from django.shortcuts import render

from movies.models import movies


def index(request):
    bannar_movie=movies.objects.filter().order_by('-id')[:5]
    random_movie = movies.objects.filter().order_by('?')[:5]
    fmovie = movies.objects.filter().order_by('-id')[5:11]
    random_movie_1 = movies.objects.filter().order_by('?')[5:11]
    recent_movie = movies.objects.filter().order_by('-id')[5:11]
    context={
        'bannar_movie':bannar_movie,
        'random_movie':random_movie,
        'featured_movie':fmovie,
        'random_movie_1':random_movie_1,
        'recent_movie':recent_movie,
    }
    return render(request,'index.html',context)