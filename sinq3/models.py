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

	image = models.ImageField(upload_to='images/')

	# Called by Django when printing objects... give it something more helpful for programers to read (pretty print).
	# def __unicode__(self):
	# 	return 'Image for ' + self.question.text

class Project(models.Model):
	name = models.TextField()
	creation_timestamp = models.DateTimeField('date published')

	#question = models.ForeignKey(Question)

	# creator (use Django authentication)

	# Called by Django when printing objects... give it something more helpful for programers to read (pretty print).
	def __unicode__(self):
		return self.name