from django.db import models
import os

class Movie(models.Model):
  name             = models.CharField(max_length=255)
  dirname          = models.CharField(max_length=255)
  format           = models.CharField(max_length=255, default="avi")
  date_added       = models.DateTimeField(auto_now_add=True)

  imdb_link        = models.TextField(null=True, blank=True)
  last_downloaded  = models.DateTimeField(null=True, blank=True)
  times_downloaded = models.PositiveIntegerField(default=0)

  def get_full_path(self):
    return os.path.join("/pants/Movies", self.dirname[0], self.dirname)
