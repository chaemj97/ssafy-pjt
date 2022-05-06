from django.shortcuts import redirect, render, get_object_or_404
# 요청 메서드에 따라 view함수에 대한 엑세스 제한
from django.views.decorators.http import require_http_methods, require_POST,require_safe

from movies.forms import MoviesForm
from .models import Movie

# Create your views here.

@ require_safe # GET
def index(request):
    movies = Movie.objects.order_by('-pk')
    context = {
        'movies':movies
    }
    return render(request,'movies/index.html',context)

@ require_http_methods(['GET','POST']) # GET,POST
def create(request):
    if request.method == 'POST': # create
        form = MoviesForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else: # new
        form = MoviesForm()
    context = {
        'form':form
    }
    return render(request,'movies/create.html',context)

@ require_safe
def detail(request,pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie':movie
    }
    return render(request,'movies/detail.html',context)

@ require_http_methods(['GET','POST'])
def update(request,pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST': # update
        form = MoviesForm(request.POST,instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail',movie.pk)
    else: # edit
        form = MoviesForm(instance=movie)
    context = {
        'movie':movie,
        'form':form
    }
    return render(request,'movies/update.html', context)

@ require_POST # POST
def delete(request,pk):
    # movie = Movie.objects.get(pk=pk)
    movie = get_object_or_404(Movie, pk=pk)
    movie.delete()
    return redirect('movies:index')
