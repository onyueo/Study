from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST

from .models import Movie, Comment
from .forms import MovieForm, CommentForm

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'moveis': movies,

    }
    return render(request, 'movies/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:detail', movie.pk)
        
    elif request.method == 'GET':
        form = MovieForm()
    context = {
        'form': form,

    }
    return redirect(request, 'movies:create.html', context)


@require_http_methods(['GET'])
def detail(request, moive_pk):
    movie = Movie.objects.get(pk=moive_pk)
    comments_form = CommentForm()
    comments = movie.comment_set.all()

    context = {
        'movie': movie,
        'comments_form': comments_form,
        'comments': comments,
    }
    return render(request, 'movies:detail.html', context)



@require_http_methods(['GET', 'POST'])
def update(request, moive_pk):
    movie = Movie.objects.get(pk=moive_pk)
    if request.user == movie.user:
        if request.method == 'POST':
            form = MovieForm(request.POST, instance=movie)
            if form.is_valid():
                form.save()
                return redirect('movies:detail', movie.pk)

        else:
            form = MovieForm(instance=movie)
    
    else:
        return redirect('movies:index')

    context = {
        'movie': movie,
        'form': form
    }
    
    return render(request, 'movies:update.html', context)


@require_http_methods(['POST'])
def delete(request, moive_pk):
    movie = Movie.objects.get(pk=moive_pk)
    if request.user == movie.user:
        movie.delete()
        return redirect('movies:index')



@require_http_methods(['POST'])
def comments_create(request, comment_pk):
    movie = Movie.objects.get(pk=comment_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        movie = movie
        comment.save()
        return redirect('movies:detail', movie.pk)

# @require_http_methods(['POST'])




# @require_http_methods(['POST'])


