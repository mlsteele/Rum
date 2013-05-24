from django.core.management.base import BaseCommand, CommandError
from web.main.models import Movie, MovieFile

import os, string

class Command(BaseCommand):
    args = '<movie_root_path>'
    help = 'Loads movies from files'

    def handle(self, *args, **options):
        def list_subdirs(path):
            return [ d for d in os.listdir(path) if not os.path.isfile(os.path.join(path, d)) ]

        def list_subfiles(path):
            return [ d for d in os.listdir(path) if os.path.isfile(os.path.join(path, d)) ]

        def load_movie_dir(movie_root):
            print "searching in movie_root=%s" % movie_root
            for letter_dir in list_subdirs(movie_root):
                print "searching in letter_dir=%s" % letter_dir
                for movie_dir in list_subdirs(os.path.join(movie_root, letter_dir)):
                    print "adding movie_dir=%s" % movie_dir
                    movie = Movie(name=movie_dir, path=os.path.join(letter_dir, movie_dir), autoloaded=True)
                    movie.save()
                    print "    saving Movie..."

                    for f in list_subfiles(os.path.join(movie_root, letter_dir, movie_dir)):
                        extension = os.path.splitext(f)[1][1:]
                        print "    adding moviefile at %s with format=%s" %(f, extension)
                        fmt = extension if len(extension) > 0 else 'unknown'
                        moviefile = MovieFile(filename=f, format=fmt, movie=movie)
                        moviefile.save()
                        print "    saving MovieFile..."
            print "Done with movies!"

        load_movie_dir(args[0])
