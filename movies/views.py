from django.shortcuts import render

# Create your views here.
from movies.models import movies


def movie(request,id):
    mov=movies.objects.get(id=id)
    random_movie_1 = movies.objects.filter().order_by('?')[:10]
    recent_movie = movies.objects.filter().order_by('-id')[:10]
    context={
        'movie':mov,
        'random_movie_1':random_movie_1,
        'recent_movie':recent_movie,
    }
    return render(request,'movie.html',context)


def all_movie(request):
    if 'word' in request.GET:
        word=request.GET['word']
        all_mov = movies.objects.filter(Title__startswith=word)
        count = movies.objects.filter(Title__startswith=word).count()
        context = {
            'all_mov': all_mov,
            'count':count,
        }
        return render(request, 'all_movie.html', context)
    elif 'search' in request.GET:
        search=request.GET['search']
        all_mov = movies.objects.filter(Title__icontains=search)
        count = movies.objects.filter(Title__icontains=search).count()
        context = {
            'all_mov': all_mov,
            'count':count,
        }
        return render(request, 'all_movie.html', context)
    else:
        all_mov = movies.objects.filter().order_by('-id')
        count=all_mov.count()
        context={
            'all_mov':all_mov,
            'count': count,
        }
        return render(request,'all_movie.html',context)



def feature(request):
    return render(request,'feature.html')