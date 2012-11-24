# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CauseAndEffectImage.causeandeffect'
        db.add_column('sinq3_causeandeffectimage', 'causeandeffect',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['sinq3.CauseAndEffect']),
                      keep_default=False)

        # Removing M2M table for field causeandeffects on 'CauseAndEffectImage'
        db.delete_table('sinq3_causeandeffectimage_causeandeffects')


    def backwards(self, orm):
        # Deleting field 'CauseAndEffectImage.causeandeffect'
        db.delete_column('sinq3_causeandeffectimage', 'causeandeffect_id')

        # Adding M2M table for field causeandeffects on 'CauseAndEffectImage'
        db.create_table('sinq3_causeandeffectimage_causeandeffects', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('causeandeffectimage', models.ForeignKey(orm['sinq3.causeandeffectimage'], null=False)),
            ('causeandeffect', models.ForeignKey(orm['sinq3.causeandeffect'], null=False))
        ))
        db.create_unique('sinq3_causeandeffectimage_causeandeffects', ['causeandeffectimage_id', 'causeandeffect_id'])


    models = {
        'sinq3.causeandeffect': {
            'Meta': {'object_name': 'CauseAndEffect'},
            'cause': ('django.db.models.fields.TextField', [], {}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'effect': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'investigations': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['sinq3.Investigation']", 'null': 'True', 'blank': 'True'}),
            'questions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['sinq3.Question']", 'null': 'True', 'blank': 'True'})
        },
        'sinq3.causeandeffectimage': {
            'Meta': {'object_name': 'CauseAndEffectImage'},
            'causeandeffect': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['sinq3.CauseAndEffect']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'sinq3.investigation': {
            'Meta': {'object_name': 'Investigation'},
            'causeandeffects': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['sinq3.CauseAndEffect']", 'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'questions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['sinq3.Question']", 'null': 'True', 'blank': 'True'})
        },
        'sinq3.investigationstep': {
            'Meta': {'object_name': 'InvestigationStep'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'investigation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'steps'", 'to': "orm['sinq3.Investigation']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'sinq3.investigationstepimage': {
            'Meta': {'object_name': 'InvestigationStepImage'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'step': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['sinq3.InvestigationStep']"})
        },
        'sinq3.question': {
            'Meta': {'object_name': 'Question'},
            'causeandeffects': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['sinq3.CauseAndEffect']", 'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'investigations': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['sinq3.Investigation']", 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'sinq3.questionimage': {
            'Meta': {'object_name': 'QuestionImage'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['sinq3.Question']"})
        }
    }

    complete_apps = ['sinq3']