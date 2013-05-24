import os
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.servers.basehttp import FileWrapper
from django.shortcuts import render
from django.dispatch import receiver
from django_browserid import signals
from django.http import HttpResponse
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

@login_required
def movie_download(request, file_pk):
    movie_file = MovieFile.objects.get(pk=file_pk)
    movie_file.last_downloaded = datetime.now()
    movie_file.times_downloaded += 1
    movie_file.save()
    # Serve the file, securely.
    file_path = os.path.join(settings.MEDIA_ROOT, movie_file.get_full_path())
    wrapper = FileWrapper(file(file_path))
    response = HttpResponse(wrapper, content_type='application/x-download')
    response['Content-Length'] = os.path.getsize(file_path)
    return response

@receiver(signals.user_created)
def user_created(sender, user, **kwargs):
    user.is_active = False
    user.save()
