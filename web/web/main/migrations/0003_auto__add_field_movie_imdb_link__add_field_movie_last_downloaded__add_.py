# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Movie.imdb_link'
        db.add_column(u'main_movie', 'imdb_link',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Movie.last_downloaded'
        db.add_column(u'main_movie', 'last_downloaded',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Movie.times_downloaded'
        db.add_column(u'main_movie', 'times_downloaded',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Movie.imdb_link'
        db.delete_column(u'main_movie', 'imdb_link')

        # Deleting field 'Movie.last_downloaded'
        db.delete_column(u'main_movie', 'last_downloaded')

        # Deleting field 'Movie.times_downloaded'
        db.delete_column(u'main_movie', 'times_downloaded')


    models = {
        u'main.movie': {
            'Meta': {'object_name': 'Movie'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dirname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'format': ('django.db.models.fields.CharField', [], {'default': "'avi'", 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imdb_link': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'last_downloaded': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'times_downloaded': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['main']