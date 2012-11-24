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
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('date_last_modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('sinq3', ['Question'])

        # Adding M2M table for field causeandeffects on 'Question'
        db.create_table('sinq3_question_causeandeffects', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('question', models.ForeignKey(orm['sinq3.question'], null=False)),
            ('causeandeffect', models.ForeignKey(orm['sinq3.causeandeffect'], null=False))
        ))
        db.create_unique('sinq3_question_causeandeffects', ['question_id', 'causeandeffect_id'])

        # Adding M2M table for field investigations on 'Question'
        db.create_table('sinq3_question_investigations', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('question', models.ForeignKey(orm['sinq3.question'], null=False)),
            ('investigation', models.ForeignKey(orm['sinq3.investigation'], null=False))
        ))
        db.create_unique('sinq3_question_investigations', ['question_id', 'investigation_id'])

        # Adding model 'QuestionImage'
        db.create_table('sinq3_questionimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['sinq3.Question'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('date_last_modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('sinq3', ['QuestionImage'])

        # Adding model 'CauseAndEffect'
        db.create_table('sinq3_causeandeffect', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cause', self.gf('django.db.models.fields.TextField')()),
            ('effect', self.gf('django.db.models.fields.TextField')()),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('date_last_modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('sinq3', ['CauseAndEffect'])

        # Adding M2M table for field questions on 'CauseAndEffect'
        db.create_table('sinq3_causeandeffect_questions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('causeandeffect', models.ForeignKey(orm['sinq3.causeandeffect'], null=False)),
            ('question', models.ForeignKey(orm['sinq3.question'], null=False))
        ))
        db.create_unique('sinq3_causeandeffect_questions', ['causeandeffect_id', 'question_id'])

        # Adding M2M table for field investigations on 'CauseAndEffect'
        db.create_table('sinq3_causeandeffect_investigations', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('causeandeffect', models.ForeignKey(orm['sinq3.causeandeffect'], null=False)),
            ('investigation', models.ForeignKey(orm['sinq3.investigation'], null=False))
        ))
        db.create_unique('sinq3_causeandeffect_investigations', ['causeandeffect_id', 'investigation_id'])

        # Adding model 'CauseAndEffectImage'
        db.create_table('sinq3_causeandeffectimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('date_last_modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('sinq3', ['CauseAndEffectImage'])

        # Adding M2M table for field causeandeffects on 'CauseAndEffectImage'
        db.create_table('sinq3_causeandeffectimage_causeandeffects', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('causeandeffectimage', models.ForeignKey(orm['sinq3.causeandeffectimage'], null=False)),
            ('causeandeffect', models.ForeignKey(orm['sinq3.causeandeffect'], null=False))
        ))
        db.create_unique('sinq3_causeandeffectimage_causeandeffects', ['causeandeffectimage_id', 'causeandeffect_id'])

        # Adding model 'Investigation'
        db.create_table('sinq3_investigation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('date_last_modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('sinq3', ['Investigation'])

        # Adding M2M table for field questions on 'Investigation'
        db.create_table('sinq3_investigation_questions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('investigation', models.ForeignKey(orm['sinq3.investigation'], null=False)),
            ('question', models.ForeignKey(orm['sinq3.question'], null=False))
        ))
        db.create_unique('sinq3_investigation_questions', ['investigation_id', 'question_id'])

        # Adding M2M table for field causeandeffects on 'Investigation'
        db.create_table('sinq3_investigation_causeandeffects', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('investigation', models.ForeignKey(orm['sinq3.investigation'], null=False)),
            ('causeandeffect', models.ForeignKey(orm['sinq3.causeandeffect'], null=False))
        ))
        db.create_unique('sinq3_investigation_causeandeffects', ['investigation_id', 'causeandeffect_id'])

        # Adding model 'InvestigationStep'
        db.create_table('sinq3_investigationstep', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('investigation', self.gf('django.db.models.fields.related.ForeignKey')(related_name='steps', to=orm['sinq3.Investigation'])),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('date_last_modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('sinq3', ['InvestigationStep'])

        # Adding model 'InvestigationStepImage'
        db.create_table('sinq3_investigationstepimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('step', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['sinq3.InvestigationStep'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('date_last_modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('sinq3', ['InvestigationStepImage'])


    def backwards(self, orm):
        # Deleting model 'Question'
        db.delete_table('sinq3_question')

        # Removing M2M table for field causeandeffects on 'Question'
        db.delete_table('sinq3_question_causeandeffects')

        # Removing M2M table for field investigations on 'Question'
        db.delete_table('sinq3_question_investigations')

        # Deleting model 'QuestionImage'
        db.delete_table('sinq3_questionimage')

        # Deleting model 'CauseAndEffect'
        db.delete_table('sinq3_causeandeffect')

        # Removing M2M table for field questions on 'CauseAndEffect'
        db.delete_table('sinq3_causeandeffect_questions')

        # Removing M2M table for field investigations on 'CauseAndEffect'
        db.delete_table('sinq3_causeandeffect_investigations')

        # Deleting model 'CauseAndEffectImage'
        db.delete_table('sinq3_causeandeffectimage')

        # Removing M2M table for field causeandeffects on 'CauseAndEffectImage'
        db.delete_table('sinq3_causeandeffectimage_causeandeffects')

        # Deleting model 'Investigation'
        db.delete_table('sinq3_investigation')

        # Removing M2M table for field questions on 'Investigation'
        db.delete_table('sinq3_investigation_questions')

        # Removing M2M table for field causeandeffects on 'Investigation'
        db.delete_table('sinq3_investigation_causeandeffects')

        # Deleting model 'InvestigationStep'
        db.delete_table('sinq3_investigationstep')

        # Deleting model 'InvestigationStepImage'
        db.delete_table('sinq3_investigationstepimage')


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
            'causeandeffects': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['sinq3.CauseAndEffect']", 'null': 'True', 'blank': 'True'}),
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