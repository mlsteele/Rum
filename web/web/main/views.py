from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.dispatch import receiver
from django_browserid import signals
from web.main.models import Movie, MovieFile

def login(request):
    return render(request, 'main/login.html')


def login_failed(request):
    return render(request, 'main/login_failed.html')


@login_required
def home(request):
    return render(request, 'main/home.html')


@login_required
def movies(request):
    movie_records = Movie.objects.all().order_by('name')
    return render(request, 'main/movies.html', {'movies': movie_records})

@login_required
def movie(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    files = movie.moviefile_set.all()
    return render(request, 'main/movie.html', {'movie': movie, 'files': files})


@receiver(signals.user_created)
def user_created(sender, user, **kwargs):
    user.is_active = False
    user.save()
