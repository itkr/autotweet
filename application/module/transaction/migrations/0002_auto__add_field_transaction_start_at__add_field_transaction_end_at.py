# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Transaction.start_at'
        db.add_column(u'transaction_transaction', 'start_at',
                      self.gf('django.db.models.fields.DateTimeField')(null=True),
                      keep_default=False)

        # Adding field 'Transaction.end_at'
        db.add_column(u'transaction_transaction', 'end_at',
                      self.gf('django.db.models.fields.DateTimeField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Transaction.start_at'
        db.delete_column(u'transaction_transaction', 'start_at')

        # Deleting field 'Transaction.end_at'
        db.delete_column(u'transaction_transaction', 'end_at')


    models = {
        'transaction.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'end_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'remaining_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': 'None', 'null': 'True'}),
            'start_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '140'}),
            'time_id': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['transaction']