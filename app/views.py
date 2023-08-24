from django.shortcuts import render
from django.http import *
from app.models import *
# Create your views here.

def movie_group(request):
    se= input('Enter a section: ')
    mv= Marvel.objects.get_or_create(movie_base=se)[0]
    mv.save()
    return HttpResponse('<center><h1> Movie Group Has Been Inserted </h></center>')

def movie_col(request):
    se= input('Enter a section: ')
    mv= Marvel.objects.get_or_create(movie_base=se)[0]
    mv.save()

    names = input('Enter your Movie/Series: ')
    url = input('Enter your platform link: ')
    date= input('Enter your upload date: ')

    col = Movies.objects.get_or_create(movie_base=mv, movie_name=names, Relese_date=date, Ott= url)[0]
    col.save()
    return HttpResponse('<center><h1> Movie Name Relese Date Ott Platform Has Been Saved </h></center>')

def act(request):
    se= input('Enter a section: ')
    mv= Marvel.objects.get_or_create(movie_base=se)[0]
    mv.save()

    names = input('Enter your Movie/Series: ')
    url = input('Enter your platform link: ')
    date= input('Enter your upload date: ')

    col = Movies.objects.get_or_create(movie_base=mv, movie_name=names, Relese_date=date, Ott= url)[0]
    col.save()

    chr = input('Enter Character Name: ')
    mm= Actor.objects.get_or_create(movie_name=col, character= chr)[0]
    mm.save()
    return HttpResponse('<center><h1> All Data Has Been Saved. </h></center>')