# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Movie'
        db.create_table(u'main_movie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('dirname', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('format', self.gf('django.db.models.fields.CharField')(default='avi', max_length=255)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['Movie'])


    def backwards(self, orm):
        # Deleting model 'Movie'
        db.delete_table(u'main_movie')


    models = {
        u'main.movie': {
            'Meta': {'object_name': 'Movie'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dirname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'format': ('django.db.models.fields.CharField', [], {'default': "'avi'", 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['main']