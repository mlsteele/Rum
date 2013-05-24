# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MovieFile'
        db.create_table(u'main_moviefile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('filename', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('format', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('movie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Movie'])),
            ('last_downloaded', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('times_downloaded', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['MovieFile'])

        # Deleting field 'Movie.times_downloaded'
        db.delete_column(u'main_movie', 'times_downloaded')

        # Deleting field 'Movie.uploader'
        db.delete_column(u'main_movie', 'uploader')

        # Deleting field 'Movie.format'
        db.delete_column(u'main_movie', 'format')

        # Deleting field 'Movie.dirname'
        db.delete_column(u'main_movie', 'dirname')

        # Deleting field 'Movie.last_downloaded'
        db.delete_column(u'main_movie', 'last_downloaded')

        # Adding field 'Movie.path'
        db.add_column(u'main_movie', 'path',
                      self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'MovieFile'
        db.delete_table(u'main_moviefile')

        # Adding field 'Movie.times_downloaded'
        db.add_column(u'main_movie', 'times_downloaded',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Movie.uploader'
        db.add_column(u'main_movie', 'uploader',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Movie.format'
        db.add_column(u'main_movie', 'format',
                      self.gf('django.db.models.fields.CharField')(default='avi', max_length=255),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Movie.dirname'
        raise RuntimeError("Cannot reverse this migration. 'Movie.dirname' and its values cannot be restored.")
        # Adding field 'Movie.last_downloaded'
        db.add_column(u'main_movie', 'last_downloaded',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Movie.path'
        db.delete_column(u'main_movie', 'path')


    models = {
        u'main.movie': {
            'Meta': {'object_name': 'Movie'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imdb_link': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'main.moviefile': {
            'Meta': {'object_name': 'MovieFile'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'format': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_downloaded': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Movie']"}),
            'times_downloaded': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['main']