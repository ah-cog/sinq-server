from django.db import models
import datetime

# SINQ database models

class Question(models.Model):
	# Relations/Dependencies
	causeandeffects = models.ManyToManyField('CauseAndEffect', blank=True, null=True)
	investigations  = models.ManyToManyField('Investigation', blank=True, null=True)

	text = models.TextField()

	# Timestamps
	# http://david.feinzeig.com/blog/2011/12/06/how-to-properly-set-a-default-value-for-a-datetimefield-in-django/
	# http://stackoverflow.com/questions/2029295/django-datefield-default-options
	date_created       = models.DateTimeField(editable=False, default=datetime.datetime.now)
	date_last_modified = models.DateTimeField(default=datetime.datetime.now)

	# def save(self, *args, **kwargs):
	# 	'''On save, update timestamps.'''
	# 	if not self.id:
	# 		self.date_created = datetime.datetime.today()
	# 	self.date_modified = datetime.datetime.today()

	# Called by Django when printing objects... give it something more helpful for programers to read (pretty print).
	def __unicode__(self):
		return self.text

class QuestionImage(models.Model):
	question = models.ForeignKey('Question', related_name='images')

	image = models.ImageField(upload_to='images/questions/')

	# Timestamps
	date_created       = models.DateTimeField(editable=False, default=datetime.datetime.now)
	date_last_modified = models.DateTimeField(default=datetime.datetime.now)




class CauseAndEffect(models.Model):
	# Relations/Dependencies
	#questions      = models.ManyToManyField('Question', blank=True, null=True)
	investigations = models.ManyToManyField('Investigation', blank=True, null=True)

	# Properties
	cause  = models.TextField()
	effect = models.TextField()

	# Timestamps
	date_created       = models.DateTimeField(editable=False, default=datetime.datetime.now)
	date_last_modified = models.DateTimeField(default=datetime.datetime.now)

	def __unicode__(self):
		return "Cause: %s => Effect: %s" % (self.cause, self.effect)

def get_default_cause_and_effect():
	return CauseAndEffect.objects.all()[0] # TODO: Create a "default" CauseAndEffect rather than one with id=1

class CauseAndEffectImage(models.Model):
	causeandeffect = models.ForeignKey('CauseAndEffect', related_name='images', default=get_default_cause_and_effect)

	image = models.ImageField(upload_to='images/causeandeffects/')

	# Timestamps
	date_created       = models.DateTimeField(editable=False, default=datetime.datetime.now)
	date_last_modified = models.DateTimeField(default=datetime.datetime.now)




class Investigation(models.Model):
	# Relations/Dependencies
	# questions       = models.ManyToManyField('Question', blank=True, null=True)
	# causeandeffects = models.ManyToManyField('CauseAndEffect', blank=True, null=True)

	# Timestamps
	date_created       = models.DateTimeField(editable=False, default=datetime.datetime.now)
	date_last_modified = models.DateTimeField(default=datetime.datetime.now)

class InvestigationStep(models.Model):
	# Dependencies
	investigation = models.ForeignKey('Investigation', related_name='steps')

	number = models.PositiveIntegerField(blank=True, null=True) # Make unique.  Make auto-increment?
	text = models.TextField()

	# Timestamps
	date_created       = models.DateTimeField(editable=False, default=datetime.datetime.now)
	date_last_modified = models.DateTimeField(default=datetime.datetime.now)

class InvestigationStepImage(models.Model):
	# Dependencies
	step = models.ForeignKey('InvestigationStep', related_name='images')

	image = models.ImageField(upload_to='images/investigations/steps/')

	# Timestamps
	date_created       = models.DateTimeField(editable=False, default=datetime.datetime.now)
	date_last_modified = models.DateTimeField(default=datetime.datetime.now)