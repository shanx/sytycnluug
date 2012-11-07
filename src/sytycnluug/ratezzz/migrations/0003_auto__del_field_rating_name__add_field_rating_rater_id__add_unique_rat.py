# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Rating.name'
        db.delete_column('ratezzz_rating', 'name')

        # Adding field 'Rating.rater_id'
        db.add_column('ratezzz_rating', 'rater_id',
                      self.gf('django.db.models.fields.CharField')(default='rater', max_length=12),
                      keep_default=False)

        # Adding unique constraint on 'Rating', fields ['rater_id', 'talk']
        db.create_unique('ratezzz_rating', ['rater_id', 'talk_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Rating', fields ['rater_id', 'talk']
        db.delete_unique('ratezzz_rating', ['rater_id', 'talk_id'])


        # User chose to not deal with backwards NULL issues for 'Rating.name'
        raise RuntimeError("Cannot reverse this migration. 'Rating.name' and its values cannot be restored.")
        # Deleting field 'Rating.rater_id'
        db.delete_column('ratezzz_rating', 'rater_id')


    models = {
        'ratezzz.rating': {
            'Meta': {'unique_together': "(('talk', 'rater_id'),)", 'object_name': 'Rating'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rater_id': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'rating': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'talk': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratezzz.Talk']"})
        },
        'ratezzz.talk': {
            'Meta': {'object_name': 'Talk'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'speakers': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['ratezzz']