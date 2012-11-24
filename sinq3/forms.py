from django import forms

class QuestionForm(forms.Form):
	question_text = forms.CharField(
		min_length=0,
		max_length=100
	)

class QuestionImageForm(forms.Form):
	question_image = forms.ImageField(
		label='Select a picture!',
		help_text='max size?'
	)

class CauseAndEffectImageForm(forms.Form):
	causeandeffect_image = forms.ImageField(
		label='Select a picture!',
		help_text='max size?'
	)