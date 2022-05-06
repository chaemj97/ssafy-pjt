import imp
from platform import release
from django.shortcuts import redirect, render
from .models import Movie
# Create your views here.
def index(request):
    movies=Movie.objects.all()
    context = {
        'movies' : movies
    }
    return render(request,'movies/index.html',context)

def new(request):
    return render(request,'movies/new.html')

def create(request):
    title = request.POST.get('title')
    audience = request.POST.get('audience')
    release_date = request.POST.get('release_date')
    genre = request.POST.get('genre')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')
    movie = Movie()
    movie.title = title
    movie.audience = audience
    movie.release_date = release_date
    movie.genre = genre
    movie.score = score
    movie.poster_url = poster_url
    movie.description = description
    movie.save()
    return redirect('movies:detail',movie.pk)

def detail(request,pk):
    movies=Movie.objects.get(pk=pk)
    context = {
        'movies' : movies
    }
    return render(request,'movies/detail.html',context)

def edit(request,pk):
    movies = Movie.objects.get(pk=pk)
    context = {
        'movies' : movies,
    }
    return render(request,'movies/edit.html',context)

def update(request,pk):
    movies = Movie.objects.get(pk=pk)
    movies.title = request.POST.get('title')
    movies.audience = request.POST.get('audience')
    movies.release_date = request.POST.get('release_date')
    movies.genre = request.POST.get('genre')
    movies.score = request.POST.get('score')
    movies.poster_url = request.POST.get('poster_url')
    movies.description = request.POST.get('description')
    movies.save()
    return redirect('movies:detail',movies.pk)

def delete(request,pk):
    movies=Movie.objects.get(pk=pk)
    movies.delete()
    return redirect('movies:index')