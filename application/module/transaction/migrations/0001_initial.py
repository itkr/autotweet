# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Transaction'
        db.create_table(u'transaction_transaction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
            ('time_id', self.gf('django.db.models.fields.IntegerField')(default=None, null=True)),
            ('text', self.gf('django.db.models.fields.TextField')(default='', max_length=140)),
            ('enable', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('remaining_count', self.gf('django.db.models.fields.PositiveIntegerField')(default=None, null=True)),
        ))
        db.send_create_signal('transaction', ['Transaction'])


    def backwards(self, orm):
        # Deleting model 'Transaction'
        db.delete_table(u'transaction_transaction')


    models = {
        'transaction.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'remaining_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': 'None', 'null': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '140'}),
            'time_id': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['transaction']