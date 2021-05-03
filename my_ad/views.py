import requests
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect


# Create your views here.
from movies.models import movies


def my_ad_login(request):
    if request.method == "POST":
        username=request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        if username == '123' and password=='123':
                messages.success(request,'lOGGED iN')
                return redirect('my-ad-home')
        else:
            messages.success(request, 'Incorrect Detail')
            return redirect('my-ad-login')
    else:
        context={}
        return render(request,'my_ad/login.html',context)

def my_ad_home(request):

    context={}
    return render(request,'my_ad/home.html',context)


def my_ad_add_movies(request):
    if request.method == "POST":
        if 'id' in request.POST:
            mid=request.POST['id']
            if movies.objects.filter(imdb_movie_id=mid).exists():
                messages.success(request,'This Movie Is Already Added')
                return redirect('my-ad-home')
            else:
                url = ('http://www.omdbapi.com/?i=' + mid + '&apikey=5e464fe3&plot=full')
                resp = requests.get(url);
                data = resp.json()
                if data['Response'] == 'False':
                    messages.success(request,data['Error'] )
                    return redirect('my-ad-home')
                else:
                    m_Title=data['Title']
                    m_Released_date = data['Released']
                    m_Runtime = data['Runtime']
                    m_Genre = data['Genre']
                    m_Director=data['Director']
                    m_Writer = data['Writer']
                    m_story_line = data['Plot']
                    m_Language = data['Language']
                    m_Country = data['Country']
                    m_Awards = data['Awards']
                    m_Poster = data['Poster']
                    movie=movies(imdb_movie_id=mid,Title=m_Title,Released=m_Released_date,Runtime=m_Runtime,Genre=m_Genre,Director=m_Director,Writer=m_Writer,story_line=m_story_line,Language=m_Language,Country=m_Country,Awards=m_Awards,Poster=m_Poster)
                    movie.save()
                    messages.success(request, 'Movie Added Successfully')
                    return redirect('my-ad-home')
        if 'title' in request.POST:
            title=request.POST['title']
            r_from = request.POST['r_from']
            r_to = request.POST['r_to']
            x=1
            main_dict={}
            for page in range(int(r_from),int(r_to)):
                url = ('http://www.omdbapi.com/?s=' + title + '&apikey=5e464fe3&page='+str(page))
                resp = requests.get(url);
                data = resp.json()
                if data['Response'] == 'False':
                      messages.success(request,data['Error'])
                      return redirect('my-ad-home')
                else:
                    main_sub_dict={}
                    for i in range(0,10):
                        main_sub_dict[i]={'title':data['Search'][i]['Title'],'imdbid':data['Search'][i]['imdbID'],'poster':data['Search'][i]['Poster']}
                    main_dict[page]=main_sub_dict

        context = {
            'search_result':main_dict,
            'is_title':title,
            'r_from':r_from,
            'r_to':r_to,
        }
        return render(request, 'my_ad/home.html', context)
    if 'imdbid' in request.GET:
        mid=request.GET['imdbid']
        if movies.objects.filter(imdb_movie_id=mid).exists():
            return JsonResponse({'status':0,'msg':'This Movie Is already Added'})
        else:
            url = ('http://www.omdbapi.com/?i=' + mid + '&apikey=5e464fe3&plot=full')
            resp = requests.get(url);
            data = resp.json()
            if data['Response'] == 'False':
                return JsonResponse({'status':0,'msg':data['Error']})
            else:
                m_Title = data['Title']
                m_Released_date = data['Released']
                m_Runtime = data['Runtime']
                m_Genre = data['Genre']
                m_Director = data['Director']
                m_Writer = data['Writer']
                m_story_line = data['Plot']
                m_Language = data['Language']
                m_Country = data['Country']
                m_Awards = data['Awards']
                m_Poster = data['Poster']
                movie = movies(imdb_movie_id=mid, Title=m_Title, Released=m_Released_date, Runtime=m_Runtime,
                               Genre=m_Genre, Director=m_Director, Writer=m_Writer, story_line=m_story_line,
                               Language=m_Language, Country=m_Country, Awards=m_Awards, Poster=m_Poster)
                movie.save()
                return JsonResponse({'status':0,'msg':'Movie Added Succcessfully'})

    else:
        return redirect('my-ad-home')
    context={}
    return render(request,'my_ad/home.html',context)


def add_all_movie(request):
    if 'title' in request.GET:
        title = request.GET['title']
        r_from = request.GET['r_from']
        r_to = request.GET['r_to']
        for page in range(int(r_from), int(r_to)):
            url = ('http://www.omdbapi.com/?s=' + title + '&apikey=5e464fe3&page=' + str(page))
            resp = requests.get(url);
            data = resp.json()
            if data['Response'] == 'False':
                messages.success(request, data['Error'])
                return redirect('my-ad-home')
            else:
                for i in range(0, 10):
                    mid=data['Search'][i]['imdbID']
                    if movies.objects.filter(imdb_movie_id=mid).exists():
                        pass
                    else:
                        url1 = ('http://www.omdbapi.com/?i='+mid+'&apikey=5e464fe3&plot=full')
                        resp1 = requests.get(url1);
                        data1 = resp1.json()
                        if data1['Response'] == 'False':
                            pass
                        else:
                            m_Title = data1['Title']
                            m_Released_date = data1['Released']
                            m_Runtime = data1['Runtime']
                            m_Genre = data1['Genre']
                            m_Director = data1['Director']
                            m_Writer = data1['Writer']
                            m_story_line = data1['Plot']
                            m_Language = data1['Language']
                            m_Country = data1['Country']
                            m_Awards = data1['Awards']
                            m_Poster = data1['Poster']
                            movie = movies(imdb_movie_id=mid, Title=m_Title, Released=m_Released_date,
                                           Runtime=m_Runtime, Genre=m_Genre, Director=m_Director, Writer=m_Writer,
                                           story_line=m_story_line, Language=m_Language, Country=m_Country,
                                           Awards=m_Awards, Poster=m_Poster)
                            movie.save()
        messages.success(request, 'All Movie Added Successfully ')
        return redirect('my-ad-home')
    return redirect('my-ad-home')