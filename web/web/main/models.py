from django.db import models
import os


class Movie(models.Model):
    LAME_FIRST_WORDS = ['a', 'the']

    name             = models.CharField(max_length=255)
    dirname          = models.CharField(max_length=255)
    format           = models.CharField(max_length=255, default="avi")
    date_added       = models.DateTimeField(auto_now_add=True)
    uploader         = models.CharField(max_length=255, blank=True, null=True)

    imdb_link        = models.TextField(null=True, blank=True)
    last_downloaded  = models.DateTimeField(null=True, blank=True)
    times_downloaded = models.PositiveIntegerField(default=0)

    def get_full_path(self):
        if self.dirname in range(10):
            return os.path.join("/pants/Movies", "0-9", self.dirname)
        else:
            return os.path.join("/pants/Movies", self.dirname[0].upper(), self.dirname)

    def make_dirname(self):
        words = self.name.split(' ')
        if words[0] in self.LAME_FIRST_WORDS:
            return ' '.join(words[1:] + words[0])
        else:
            return ' '.join(words)
