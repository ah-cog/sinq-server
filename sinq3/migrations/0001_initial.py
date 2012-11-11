# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Question'
        db.create_table('sinq3_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('sinq3', ['Question'])

        # Adding model 'QuestionImage'
        db.create_table('sinq3_questionimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['sinq3.Question'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('sinq3', ['QuestionImage'])

        # Adding model 'QuestionVideo'
        db.create_table('sinq3_questionvideo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(related_name='videos', to=orm['sinq3.Question'])),
            ('video', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('sinq3', ['QuestionVideo'])

        # Adding model 'Hypothesis'
        db.create_table('sinq3_hypothesis', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cause', self.gf('django.db.models.fields.TextField')()),
            ('effect', self.gf('django.db.models.fields.TextField')()),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('sinq3', ['Hypothesis'])

        # Adding M2M table for field question on 'Hypothesis'
        db.create_table('sinq3_hypothesis_question', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('hypothesis', models.ForeignKey(orm['sinq3.hypothesis'], null=False)),
            ('question', models.ForeignKey(orm['sinq3.question'], null=False))
        ))
        db.create_unique('sinq3_hypothesis_question', ['hypothesis_id', 'question_id'])

        # Adding model 'HypothesisImage'
        db.create_table('sinq3_hypothesisimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hypothesis', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['sinq3.Hypothesis'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('sinq3', ['HypothesisImage'])

        # Adding model 'HypothesisVideo'
        db.create_table('sinq3_hypothesisvideo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('video', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('sinq3', ['HypothesisVideo'])

        # Adding M2M table for field hypothesis on 'HypothesisVideo'
        db.create_table('sinq3_hypothesisvideo_hypothesis', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('hypothesisvideo', models.ForeignKey(orm['sinq3.hypothesisvideo'], null=False)),
            ('hypothesis', models.ForeignKey(orm['sinq3.hypothesis'], null=False))
        ))
        db.create_unique('sinq3_hypothesisvideo_hypothesis', ['hypothesisvideo_id', 'hypothesis_id'])

        # Adding model 'Project'
        db.create_table('sinq3_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hypothesis', self.gf('django.db.models.fields.related.ForeignKey')(related_name='projects', to=orm['sinq3.Hypothesis'])),
            ('creation_timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_modification_timestamp', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('sinq3', ['Project'])

        # Adding model 'ProjectInstruction'
        db.create_table('sinq3_projectinstruction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='instructions', to=orm['sinq3.Project'])),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('sinq3', ['ProjectInstruction'])

        # Adding model 'ProjectInstructionImage'
        db.create_table('sinq3_projectinstructionimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project_instruction', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['sinq3.ProjectInstruction'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('sinq3', ['ProjectInstructionImage'])

        # Adding model 'ProjectInstructionVideo'
        db.create_table('sinq3_projectinstructionvideo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project_instruction', self.gf('django.db.models.fields.related.ForeignKey')(related_name='videos', to=orm['sinq3.ProjectInstruction'])),
            ('video', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('sinq3', ['ProjectInstructionVideo'])


    def backwards(self, orm):
        # Deleting model 'Question'
        db.delete_table('sinq3_question')

        # Deleting model 'QuestionImage'
        db.delete_table('sinq3_questionimage')

        # Deleting model 'QuestionVideo'
        db.delete_table('sinq3_questionvideo')

        # Deleting model 'Hypothesis'
        db.delete_table('sinq3_hypothesis')

        # Removing M2M table for field question on 'Hypothesis'
        db.delete_table('sinq3_hypothesis_question')

        # Deleting model 'HypothesisImage'
        db.delete_table('sinq3_hypothesisimage')

        # Deleting model 'HypothesisVideo'
        db.delete_table('sinq3_hypothesisvideo')

        # Removing M2M table for field hypothesis on 'HypothesisVideo'
        db.delete_table('sinq3_hypothesisvideo_hypothesis')

        # Deleting model 'Project'
        db.delete_table('sinq3_project')

        # Deleting model 'ProjectInstruction'
        db.delete_table('sinq3_projectinstruction')

        # Deleting model 'ProjectInstructionImage'
        db.delete_table('sinq3_projectinstructionimage')

        # Deleting model 'ProjectInstructionVideo'
        db.delete_table('sinq3_projectinstructionvideo')


    models = {
        'sinq3.hypothesis': {
            'Meta': {'object_name': 'Hypothesis'},
            'cause': ('django.db.models.fields.TextField', [], {}),
            'effect': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['sinq3.Question']", 'null': 'True', 'blank': 'True'}),
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