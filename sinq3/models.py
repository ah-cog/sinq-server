import datetime
from django.db import models

# Create SINQ models here.

class Question(models.Model):
	text = models.TextField()

	# Called by Django when printing objects... give it something more helpful for programers to read (pretty print).
	def __unicode__(self):
		return self.text

class QuestionImage(models.Model):
	question = models.ForeignKey('Question', related_name='images')

	image = models.ImageField(upload_to='images/questions/')

class QuestionVideo(models.Model):
	question = models.ForeignKey('Question', related_name='videos')

	video = models.FileField(upload_to='videos/questions/')

class Hypothesis(models.Model):
	# Dependencies (i.e., parent)
	questions = models.ManyToManyField('Question', blank=True, null=True)

	# Properties
	cause = models.TextField()
	effect = models.TextField()

	text = models.TextField()

	def __unicode__(self):
		return "Cause: %s => Effect: %s" % (self.cause, self.effect)

class HypothesisImage(models.Model):
	#hypothesis = models.ManyToManyField('Hypothesis')
	hypothesis = models.ForeignKey('Hypothesis', related_name='images')

	image = models.ImageField(upload_to='images/hypotheses/')

class HypothesisVideo(models.Model):
	hypothesis = models.ManyToManyField('Hypothesis')

	video = models.FileField(upload_to='videos/questions/')

class Project(models.Model):
	# Dependencies (i.e., parent)
	hypothesis = models.ForeignKey('Hypothesis', related_name='projects')

	# name = models.TextField()

	creation_timestamp = models.DateTimeField('date published')
	last_modification_timestamp = models.DateTimeField('date created')

	# Called by Django when printing objects... give it something more helpful for programers to read (pretty print).
	# def __unicode__(self):
	# 	return self.name

class ProjectInstruction(models.Model):
	# Dependencies
	project = models.ForeignKey('Project', related_name='instructions')

	text = models.TextField()

class ProjectInstructionImage(models.Model):
	# Dependencies
	project_instruction = models.ForeignKey('ProjectInstruction', related_name='images')

	image = models.ImageField(upload_to='images/projects/instructions/')

class ProjectInstructionVideo(models.Model):
	project_instruction = models.ForeignKey('ProjectInstruction', related_name='videos')

	video = models.FileField(upload_to='videos/projects/instructions')