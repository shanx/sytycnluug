# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Talk'
        db.create_table('ratezzz_talk', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, db_index=True)),
            ('speakers', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('ratezzz', ['Talk'])


    def backwards(self, orm):
        # Deleting model 'Talk'
        db.delete_table('ratezzz_talk')


    models = {
        'ratezzz.talk': {
            'Meta': {'object_name': 'Talk'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'speakers': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['ratezzz']