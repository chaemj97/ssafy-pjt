from django.shortcuts import redirect, render,get_object_or_404
from .models import Movie,Comment
from .forms import CommentForm, MovieForm

# Create your views here.
def index(request):
    movies = Movie.objects.order_by('-pk')
    context = {
        'movies':movies
    }
    return render(request,'movies/index.html',context)

def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:detail',movie.pk)
    else:
        form = MovieForm()
    context = {
        'form':form
    }
    return render(request,'movies/create.html',context)

def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'movie' : movie,
        'form' : form,
    }
    return render(request, 'movies/update.html', context)

def detail(request,pk):
    movie = get_object_or_404(Movie,pk=pk)
    comments = movie.comment_set.all()
    comment_form = CommentForm()
    context = {
        'movie':movie,
        'comments':comments,
        'comment_form':comment_form,
    }
    return render(request,'movies/detail.html',context)



def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')

def comments_create(request, pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            movie = get_object_or_404(Movie,pk=pk)
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.movie = movie
                comment.user = request.user
                comment.save()
            return redirect('movies:detail', movie.pk)
    return redirect('accounts:login')

def comments_delete(request, movie_pk, comment_pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            comment = get_object_or_404(Comment,pk=comment_pk)
            if request.user == comment.user:
                comment.delete()
    return redirect('movies:detail', movie_pk)
            