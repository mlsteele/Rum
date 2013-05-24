from django.db import models
import os

class Movie(models.Model):
    MOVIE_ROOT = "/pants/Movies"

    name         = models.CharField(max_length=255)
    path         = models.CharField(max_length=255) # path relative to MOVIE_ROOT to movie directory

    imdb_link    = models.TextField(null=True, blank=True)

    autoloaded   = models.BooleanField(default=False)
    date_added   = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    def get_full_path(self):
        return os.path.join(self.MOVIE_ROOT, self.path)

class MovieFile(models.Model):
    filename         = models.CharField(max_length=255) # filename (or path) relative to movie path
    format           = models.CharField(max_length=255, default="unknown")
    movie            = models.ForeignKey(Movie)

    # uploader       = models.CharField(max_length=255, blank=True, null=True)
    last_downloaded  = models.DateTimeField(null=True, blank=True)
    times_downloaded = models.PositiveIntegerField(default=0)

    date_added       = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.movie.name) + ' ' + self.get_full_path()

    def get_full_path(self):
        return os.path.join(self.movie.get_full_path(), self.filename)
