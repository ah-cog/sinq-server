# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field question on 'Hypothesis'
        db.delete_table('sinq3_hypothesis_question')

        # Adding M2M table for field questions on 'Hypothesis'
        db.create_table('sinq3_hypothesis_questions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('hypothesis', models.ForeignKey(orm['sinq3.hypothesis'], null=False)),
            ('question', models.ForeignKey(orm['sinq3.question'], null=False))
        ))
        db.create_unique('sinq3_hypothesis_questions', ['hypothesis_id', 'question_id'])


    def backwards(self, orm):
        # Adding M2M table for field question on 'Hypothesis'
        db.create_table('sinq3_hypothesis_question', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('hypothesis', models.ForeignKey(orm['sinq3.hypothesis'], null=False)),
            ('question', models.ForeignKey(orm['sinq3.question'], null=False))
        ))
        db.create_unique('sinq3_hypothesis_question', ['hypothesis_id', 'question_id'])

        # Removing M2M table for field questions on 'Hypothesis'
        db.delete_table('sinq3_hypothesis_questions')


    models = {
        'sinq3.hypothesis': {
            'Meta': {'object_name': 'Hypothesis'},
            'cause': ('django.db.models.fields.TextField', [], {}),
            'effect': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'questions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['sinq3.Question']", 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'sinq3.hypothesisimage': {
            'Meta': {'object_name': 'HypothesisImage'},
            'hypothesis': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['sinq3.Hypothesis']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'sinq3.hypothesisvideo': {
            'Meta': {'object_name': 'HypothesisVideo'},
            'hypothesis': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sinq3.Hypothesis']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'video': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'sinq3.project': {
            'Meta': {'object_name': 'Project'},
            'creation_timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'hypothesis': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects'", 'to': "orm['sinq3.Hypothesis']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modification_timestamp': ('django.db.models.fields.DateTimeField', [], {})
        },
        'sinq3.projectinstruction': {
            'Meta': {'object_name': 'ProjectInstruction'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'instructions'", 'to': "orm['sinq3.Project']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'sinq3.projectinstructionimage': {
            'Meta': {'object_name': 'ProjectInstructionImage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'project_instruction': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['sinq3.ProjectInstruction']"})
        },
        'sinq3.projectinstructionvideo': {
            'Meta': {'object_name': 'ProjectInstructionVideo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project_instruction': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'videos'", 'to': "orm['sinq3.ProjectInstruction']"}),
            'video': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'sinq3.question': {
            'Meta': {'object_name': 'Question'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'sinq3.questionimage': {
            'Meta': {'object_name': 'QuestionImage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['sinq3.Question']"})
        },
        'sinq3.questionvideo': {
            'Meta': {'object_name': 'QuestionVideo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'videos'", 'to': "orm['sinq3.Question']"}),
            'video': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['sinq3']