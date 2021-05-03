"""free_movies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from my_ad import views

urlpatterns = [
    path('my-ad-login',views.my_ad_login,name='my-ad-login'),
    path('my-ad-home', views.my_ad_home, name='my-ad-home'),
    path('my-ad-add-movies', views.my_ad_add_movies, name='my-ad-add-movies'),
path('add-all-movie', views.add_all_movie, name='add-all-movie'),
]
