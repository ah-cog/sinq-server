from sinq3.models import Question
from sinq3.models import QuestionImage

from sinq3.models import CauseAndEffect
from sinq3.models import CauseAndEffectImage

from sinq3.models import Investigation
from sinq3.models import InvestigationStep
from sinq3.models import InvestigationStepImage

from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import Context, loader

from django.template import RequestContext

from django.http import Http404

from django.shortcuts import render_to_response

# Import forms:
from sinq3.forms import QuestionForm
from sinq3.forms import QuestionImageForm
from sinq3.forms import CauseAndEffectImageForm

from django.utils import simplejson
from django.core import serializers

# For @csrf_exempt decorator (https://docs.djangoproject.com/en/1.2/ref/contrib/csrf/#exceptions).  This is needed for POSTs that do not have a CSRF token (generated by Django).
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
	# t = loader.get_template('home.html')
	# c = Context({})
	# return HttpResponse(t.render(c))



	# Retreive request data
	format = request.GET['format'] if 'format' in request.GET else None

	# latest_question_list = Question.objects.all()
	#.order_by('-creation_timestamp')[:5]

	#if len(latest_question_list) > 0: # this is not efficient, use next line:
	# if latest_question_list.count() > 0:
	# 	output = ', '.join([q.text for q in latest_question_list])
	# else:
	# 	output = 'No questions!'
	t = loader.get_template('home.html')
	# c = Context({
	# 		'latest_question_list': latest_question_list,
	# 		'format': format
	# 	})
	c = Context({})
	return HttpResponse(t.render(c))

@csrf_exempt
def question_index(request):
	if request.method == 'GET':

		# Retreive request data
		format = request.GET['format'] if 'format' in request.GET else None

		latest_question_list = Question.objects.all()
		#.order_by('-creation_timestamp')[:5]

		if format == 'json':
			# Serialize questions in JSON format
			# i.e., https://docs.djangoproject.com/en/dev/topics/serialization/
			serialized_questions = serializers.serialize('json', latest_question_list, fields=('text, preview'))
			response = HttpResponse(serialized_questions, mimetype="application/json")
			response['Access-Control-Allow-Origin'] = '*'
			return response


		else:
			#if len(latest_question_list) > 0: # this is not efficient, use next line:
			if latest_question_list.count() > 0:
				output = ', '.join([q.text for q in latest_question_list])
			else:
				output = 'No questions!'
			t = loader.get_template('questions/index.html')
			c = Context({
					'latest_question_list': latest_question_list,
					'format': format
				})
			return HttpResponse(t.render(c))

	elif request.method == 'OPTIONS':
		# Enable CORS (Cross-Origin Resource Sharing)
		# http://enable-cors.org/#how-gae
		# - This must be added to headers to enable requests from origins other 
		#   than Google (i.e., wherever students host their websites).
		#self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		response = HttpResponse()
		response['Access-Control-Allow-Origin'] = '*'
		
		# Enable access to the DELETE HTTP request method cross-origin
		# http://www.w3.org/TR/cors/#introduction
		response['Access-Control-Max-Age'] = '3600'
		#response['Access-Control-Allow-Methods'] = 'DELETE'

def question_create(request):
	if request.method == 'POST':
		form = QuestionForm(request.POST, request.FILES)
		if form.is_valid():
			# Create new question image and store in DB
			question_text = request.POST['question_text']

			question = Question(text = question_text)
			question.save()

			return HttpResponseRedirect(reverse('sinq3.views.question_view', args=(question.id,)))
	else:
		form = QuestionForm() # An empty, unbound form

	return render_to_response(
			'questions/question_create.html',
			{
				'form': form
			},
			context_instance=RequestContext(request)
		)

@csrf_exempt
def questions_read_api(request):
	if request.method == 'GET':

		# Retreive request data
		format = request.GET['format'] if 'format' in request.GET else None
		causeandeffect_id = request.GET['causeandeffect_id'] if 'causeandeffect_id' in request.GET else None
		investigation_id = request.GET['investigation_id'] if 'investigation_id' in request.GET else None

		latest_investigation_list = Investigation.objects.all()

		latest_question_list = Question.objects.all() #.order_by('-date_last_modified')[:5]

		# Create association to cause-and-effect
		if causeandeffect_id != None:
			latest_question_list = latest_question_list.filter(causeandeffects__pk=causeandeffect_id)

		# Create association to cause-and-effect
		if investigation_id != None:
			latest_question_list = latest_question_list.filter(investigations__pk=investigation_id)

		# Serialize questions in JSON format
		# i.e., https://docs.djangoproject.com/en/dev/topics/serialization/
		serialized_questions = serializers.serialize('json', latest_question_list, fields=('text'))
		response = HttpResponse(serialized_questions, mimetype="application/json")
		response['Access-Control-Allow-Origin'] = '*'
		return response

	elif request.method == 'OPTIONS':
		# Enable CORS (Cross-Origin Resource Sharing)
		# http://enable-cors.org/#how-gae
		# - This must be added to headers to enable requests from origins other 
		#   than Google (i.e., wherever students host their websites).
		#self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		response = HttpResponse()
		response['Access-Control-Allow-Origin'] = '*'
		
		# Enable access to the DELETE HTTP request method cross-origin
		# http://www.w3.org/TR/cors/#introduction
		response['Access-Control-Max-Age'] = '3600'
		#response['Access-Control-Allow-Methods'] = 'DELETE'

@csrf_exempt
def causeandeffects_read_api(request):
	if request.method == 'GET':

		# Retreive request data
		format = request.GET['format'] if 'format' in request.GET else None
		question_id = request.GET['question_id'] if 'question_id' in request.GET else None
		investigation_id = request.GET['investigation_id'] if 'investigation_id' in request.GET else None

		latest_causeandeffect_list = CauseAndEffect.objects.all()

		# Create association to question
		if question_id != None:
			latest_causeandeffect_list = latest_causeandeffect_list.filter(question__pk=question_id)

		# Create association to cause-and-effect
		if investigation_id != None:
			latest_causeandeffect_list = latest_causeandeffect_list.filter(investigations__pk=investigation_id)

		# Serialize questions in JSON format
		# i.e., https://docs.djangoproject.com/en/dev/topics/serialization/
		serialized_causeandeffects = serializers.serialize('json', latest_causeandeffect_list, fields=('cause', 'effect'))
		response = HttpResponse(serialized_causeandeffects, mimetype="application/json")
		response['Access-Control-Allow-Origin'] = '*'
		return response

	elif request.method == 'OPTIONS':
		# Enable CORS (Cross-Origin Resource Sharing)
		# http://enable-cors.org/#how-gae
		# - This must be added to headers to enable requests from origins other 
		#   than Google (i.e., wherever students host their websites).
		#self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		response = HttpResponse()
		response['Access-Control-Allow-Origin'] = '*'
		
		# Enable access to the DELETE HTTP request method cross-origin
		# http://www.w3.org/TR/cors/#introduction
		response['Access-Control-Max-Age'] = '3600'
		#response['Access-Control-Allow-Methods'] = 'DELETE'

@csrf_exempt
def question_create_api(request):
	if request.method == 'POST':

		question_json = request.body
		json_data = simplejson.loads(question_json)

		try:
			#data = json_data[0]
			question_data = json_data['question']

			question = Question(text = question_data['text'])
			question.save()

			if question_data.has_key('causeandeffect_id'):
				causeandeffect = CauseAndEffect.objects.get(id=question_data['causeandeffect_id'])
				if causeandeffect:
					question.causeandeffects.add(causeandeffect)

			if question_data.has_key('investigation_id'):
				investigation = Investigation.objects.get(id=question_data['investigation_id'])
				if investigation:
					question.investigations.add(investigation)

			# Serialize questions in JSON format
			# i.e., https://docs.djangoproject.com/en/dev/topics/serialization/
			serialized_questions = serializers.serialize('json', [question], fields=('text'))
			return HttpResponse(serialized_questions, mimetype="application/json")

		except KeyError:
			HttpResponseServerError("Malformed data!")

		return HttpResponse(object)

	else:
		HttpResponseServerError("Not POST.  Must POST to this URL.")


def question_edit(request, question_id):
	try:
		question = Question.objects.get(id=question_id)
	except:
		raise Http404

	if request.method == 'POST':
		form = QuestionForm(request.POST)
		if form.is_valid():
			# Update question properties
			question.text = request.POST['question_text']
			question.save()

			return HttpResponseRedirect(reverse('sinq3.views.question_view', args=(question.id,)))
	else:
		form = QuestionForm() # An empty, unbound form

	return render_to_response(
			'questions/question_edit.html',
			{
				'question': question,
				'form': form
			},
			context_instance=RequestContext(request)
		)

@csrf_exempt
def question_read(request, question_id):

	if request.method == 'GET':
		try:
			question = Question.objects.get(id=question_id)
		except:
			raise Http404

		# Retreive request data
		format = request.GET['format'] if 'format' in request.GET else None

		if format == 'json':
			# Serialize questions in JSON format
			# i.e., https://docs.djangoproject.com/en/dev/topics/serialization/
			serialized_questions = serializers.serialize('json', [question], fields=('text'))
			response = HttpResponse(serialized_questions, mimetype="application/json")
			response['Access-Control-Allow-Origin'] = '*'
			return response

		else:
			# Display the question
			t = loader.get_template('questions/question_view.html')
			c = Context({
					'question': question
				})

			return HttpResponse(t.render(c))

	elif request.method == 'OPTIONS':
		# Enable CORS (Cross-Origin Resource Sharing)
		# http://enable-cors.org/#how-gae
		# - This must be added to headers to enable requests from origins other 
		#   than Google (i.e., wherever students host their websites).
		#self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		response = HttpResponse()
		response['Access-Control-Allow-Origin'] = '*'
		
		# Enable access to the DELETE HTTP request method cross-origin
		# http://www.w3.org/TR/cors/#introduction
		response['Access-Control-Max-Age'] = '3600'
		#response['Access-Control-Allow-Methods'] = 'DELETE'

def question_image_create(request, question_id):
	# Get question to which the image will be attached.
	try:
		question = Question.objects.get(id=question_id)
	except:
		raise Http404

	# Save photo if POST
	if request.method == 'POST':
		form = QuestionImageForm(request.POST, request.FILES)

		if form.is_valid():
			# Create new question image and store in DB
			new_question_image          = QuestionImage(image = request.FILES['question_image'])
			new_question_image.question = question
			new_question_image.save()

			return HttpResponseRedirect(reverse('sinq3.views.question_view', args=(question.id,)))
	else:
		form = QuestionImageForm() # An empty, unbound form

	return render_to_response(
			'question_images/create.html',
			{
				'question': question,
				'form': form
			},
			context_instance=RequestContext(request)
		)

@csrf_exempt
def question_image_create_api(request, question_id):
	# Get question to which the image will be attached.
	try:
		question = Question.objects.get(id=question_id)
	except:
		raise Http404

	# Save photo if POST
	if request.method == 'POST':
		form = QuestionImageForm(request.POST, request.FILES)

		if form.is_valid():
			# Create new question image and store in DB
			new_question_image          = QuestionImage()
			new_question_image.image    = request.FILES['question_image']
			new_question_image.question = question
			new_question_image.save()
			# if request.FILES.has_key('causeandeffect_image'):
			# 	return HttpResponse('its there', mimetype="text/plain")
			# else:
			# 	return HttpResponse('nope', mimetype="text/plain")

			# Serialize questions in JSON format
			# i.e., https://docs.djangoproject.com/en/dev/topics/serialization/
			serialized_question_image = serializers.serialize('json', [new_question_image], fields=('text'))
			return HttpResponse(serialized_question_image, mimetype="application/json")
	else:
		raise Http500

@csrf_exempt
def causeandeffect_read(request, causeandeffect_id):

	if request.method == 'GET':
		try:
			causeandeffect = CauseAndEffect.objects.get(id=causeandeffect_id)
		except:
			raise Http404

		# Retreive request data
		format = request.GET['format'] if 'format' in request.GET else None

		if format == 'json':
			# Serialize questions in JSON format
			# i.e., https://docs.djangoproject.com/en/dev/topics/serialization/
			serialized_causeandeffects = serializers.serialize('json', [causeandeffect], fields=('cause', 'effect'))
			response = HttpResponse(serialized_causeandeffects, mimetype="application/json")
			response['Access-Control-Allow-Origin'] = '*'
			return response

		else:
			# Display the question
			t = loader.get_template('causeandeffects/causeandeffect_view.html')
			c = Context({
					'causeandeffect': causeandeffect
				})

			return HttpResponse(t.render(c))

	elif request.method == 'OPTIONS':
		# Enable CORS (Cross-Origin Resource Sharing)
		# http://enable-cors.org/#how-gae
		# - This must be added to headers to enable requests from origins other 
		#   than Google (i.e., wherever students host their websites).
		#self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		response = HttpResponse()
		response['Access-Control-Allow-Origin'] = '*'
		
		# Enable access to the DELETE HTTP request method cross-origin
		# http://www.w3.org/TR/cors/#introduction
		response['Access-Control-Max-Age'] = '3600'
		#response['Access-Control-Allow-Methods'] = 'DELETE'

@csrf_exempt
def causeandeffect_read_api(request, causeandeffect_id):

	if request.method == 'GET':
		try:
			causeandeffect = CauseAndEffect.objects.get(id=causeandeffect_id)
		except:
			raise Http404

		# Retreive request data
		format = request.GET['format'] if 'format' in request.GET else None

		if format == 'json':
			# Serialize questions in JSON format
			# i.e., https://docs.djangoproject.com/en/dev/topics/serialization/
			serialized_causeandeffects = serializers.serialize('json', [causeandeffect], fields=('cause', 'effect'))
			response = HttpResponse(serialized_causeandeffects, mimetype="application/json")
			response['Access-Control-Allow-Origin'] = '*'
			return response

		else:
			raise Http404

	elif request.method == 'OPTIONS':
		# Enable CORS (Cross-Origin Resource Sharing)
		# http://enable-cors.org/#how-gae
		# - This must be added to headers to enable requests from origins other 
		#   than Google (i.e., wherever students host their websites).
		#self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		response = HttpResponse()
		response['Access-Control-Allow-Origin'] = '*'
		
		# Enable access to the DELETE HTTP request method cross-origin
		# http://www.w3.org/TR/cors/#introduction
		response['Access-Control-Max-Age'] = '3600'
		#response['Access-Control-Allow-Methods'] = 'DELETE'

@csrf_exempt
def causeandeffect_image_create_api(request, causeandeffect_id):
	# Get question to which the image will be attached.
	try:
		causeandeffect = CauseAndEffect.objects.get(id=causeandeffect_id)
	except:
		raise Http404

	# Save photo if POST
	if request.method == 'POST':
		form = CauseAndEffectImageForm(request.POST, request.FILES)

		if form.is_valid():
			# Create new question image and store in DB
			new_causeandeffect_image          = CauseAndEffectImage()
			new_causeandeffect_image.image    = request.FILES['causeandeffect_image']
			new_causeandeffect_image.causeandeffect = causeandeffect
			new_causeandeffect_image.save()
			# if request.FILES.has_key('causeandeffect_image'):
			# 	return HttpResponse('its there', mimetype="text/plain")
			# else:
			# 	return HttpResponse('nope', mimetype="text/plain")

			# Serialize questions in JSON format
			# i.e., https://docs.djangoproject.com/en/dev/topics/serialization/
			serialized_causeandeffect_image = serializers.serialize('json', [new_causeandeffect_image], fields=('text'))
			return HttpResponse(serialized_causeandeffect_image, mimetype="application/json")
	else:
		raise Http500

def question_image_read(request, question_id):
	if request.method == 'GET':
		try:
			question = Question.objects.get(id=question_id)
			question_images = QuestionImage.objects.filter(question_id=question.id)
		except:
			raise Http404

		# Retreive request data
		format = request.GET['format'] if 'format' in request.GET else None

		if format == 'json':
			# Serialize questions in JSON format
			# i.e., https://docs.djangoproject.com/en/dev/topics/serialization/
			serialized_questions = serializers.serialize('json', question_images)
			response = HttpResponse(serialized_questions, mimetype="application/json")
			response['Access-Control-Allow-Origin'] = '*'
			return response

	elif request.method == 'OPTIONS':
		# Enable CORS (Cross-Origin Resource Sharing)
		# http://enable-cors.org/#how-gae
		# - This must be added to headers to enable requests from origins other 
		#   than Google (i.e., wherever students host their websites).
		#self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		response = HttpResponse()
		response['Access-Control-Allow-Origin'] = '*'
		
		# Enable access to the DELETE HTTP request method cross-origin
		# http://www.w3.org/TR/cors/#introduction
		response['Access-Control-Max-Age'] = '3600'
		#response['Access-Control-Allow-Methods'] = 'DELETE'

@csrf_exempt
def question_image_read_api(request, question_id):
	if request.method == 'GET':
		try:
			question = Question.objects.get(id=question_id)
			question_images = QuestionImage.objects.filter(question_id=question.id)
		except:
			raise Http404

		# Retreive request data
		format = request.GET['format'] if 'format' in request.GET else None

		# Serialize questions in JSON format
		# i.e., https://docs.djangoproject.com/en/dev/topics/serialization/
		serialized_questions = serializers.serialize('json', question_images)
		response = HttpResponse(serialized_questions, mimetype="application/json")
		response['Access-Control-Allow-Origin'] = '*'
		return response

	elif request.method == 'OPTIONS':
		# Enable CORS (Cross-Origin Resource Sharing)
		# http://enable-cors.org/#how-gae
		# - This must be added to headers to enable requests from origins other 
		#   than Google (i.e., wherever students host their websites).
		#self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		response = HttpResponse()
		response['Access-Control-Allow-Origin'] = '*'
		
		# Enable access to the DELETE HTTP request method cross-origin
		# http://www.w3.org/TR/cors/#introduction
		response['Access-Control-Max-Age'] = '3600'
		#response['Access-Control-Allow-Methods'] = 'DELETE'

@csrf_exempt
def investigation_step_read_api(request, investigation_id):
	if request.method == 'GET':
		try:
			investigation = Investigation.objects.get(id=investigation_id)
			investigation_steps = InvestigationStep.objects.filter(investigation_id=investigation.id).order_by('number')
		except:
			raise Http404

		# Retreive request data
		format = request.GET['format'] if 'format' in request.GET else None

		# Serialize questions in JSON format
		# i.e., https://docs.djangoproject.com/en/dev/topics/serialization/
		serialized_investigation_steps = serializers.serialize('json', investigation_steps)
		response = HttpResponse(serialized_investigation_steps, mimetype="application/json")
		response['Access-Control-Allow-Origin'] = '*'
		return response

	elif request.method == 'OPTIONS':
		# Enable CORS (Cross-Origin Resource Sharing)
		# http://enable-cors.org/#how-gae
		# - This must be added to headers to enable requests from origins other 
		#   than Google (i.e., wherever students host their websites).
		#self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		response = HttpResponse()
		response['Access-Control-Allow-Origin'] = '*'
		
		# Enable access to the DELETE HTTP request method cross-origin
		# http://www.w3.org/TR/cors/#introduction
		response['Access-Control-Max-Age'] = '3600'
		#response['Access-Control-Allow-Methods'] = 'DELETE'

@csrf_exempt
def causeandeffect_image_read_api(request, causeandeffect_id):
	if request.method == 'GET':
		try:
			causeandeffect = CauseAndEffect.objects.get(id=causeandeffect_id)
			causeandeffect_images = CauseAndEffectImage.objects.filter(causeandeffect_id=causeandeffect.id)
		except:
			raise Http404

		# Retreive request data
		format = request.GET['format'] if 'format' in request.GET else None

		# Serialize questions in JSON format
		# i.e., https://docs.djangoproject.com/en/dev/topics/serialization/
		serialized_causeandeffect_images = serializers.serialize('json', causeandeffect_images)
		response = HttpResponse(serialized_causeandeffect_images, mimetype="application/json")
		response['Access-Control-Allow-Origin'] = '*'
		return response

	elif request.method == 'OPTIONS':
		# Enable CORS (Cross-Origin Resource Sharing)
		# http://enable-cors.org/#how-gae
		# - This must be added to headers to enable requests from origins other 
		#   than Google (i.e., wherever students host their websites).
		#self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		response = HttpResponse()
		response['Access-Control-Allow-Origin'] = '*'
		
		# Enable access to the DELETE HTTP request method cross-origin
		# http://www.w3.org/TR/cors/#introduction
		response['Access-Control-Max-Age'] = '3600'
		#response['Access-Control-Allow-Methods'] = 'DELETE'

@csrf_exempt
def causeandeffects_index(request):
	if request.method == 'GET':

		# Retreive request data
		format = request.GET['format'] if 'format' in request.GET else None

		latest_causeandeffect_list = CauseAndEffect.objects.all()
		#.order_by('-creation_timestamp')[:5]

		if format == 'json':
			# Serialize questions in JSON format
			# i.e., https://docs.djangoproject.com/en/dev/topics/serialization/
			serialized_causeandeffects = serializers.serialize('json', latest_causeandeffect_list, fields=('cause', 'effect'))
			response = HttpResponse(serialized_causeandeffects, mimetype="application/json")
			response['Access-Control-Allow-Origin'] = '*'
			return response


		else:
			#if len(latest_question_list) > 0: # this is not efficient, use next line:
			if latest_causeandeffect_list.count() > 0:
				output = ', '.join([q.text for q in latest_causeandeffect_list])
			else:
				output = 'No cause-and-effects!'
			t = loader.get_template('causeandeffects/index.html')
			c = Context({
					'latest_causeandeffect_list': latest_causeandeffect_list,
					'format': format
				})
			return HttpResponse(t.render(c))

	elif request.method == 'OPTIONS':
		# Enable CORS (Cross-Origin Resource Sharing)
		# http://enable-cors.org/#how-gae
		# - This must be added to headers to enable requests from origins other 
		#   than Google (i.e., wherever students host their websites).
		#self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		response = HttpResponse()
		response['Access-Control-Allow-Origin'] = '*'
		
		# Enable access to the DELETE HTTP request method cross-origin
		# http://www.w3.org/TR/cors/#introduction
		response['Access-Control-Max-Age'] = '3600'
		#response['Access-Control-Allow-Methods'] = 'DELETE'

@csrf_exempt
def causeandeffect_create_api(request):
	if request.method == 'POST':

		causeandeffect_json = request.body
		json_data = simplejson.loads(causeandeffect_json)

		try:
			#data = json_data[0]
			causeandeffect_data = json_data['causeandeffect']

			# return HttpResponse(causeandeffect_json)

			causeandeffect = CauseAndEffect(cause = causeandeffect_data['cause_text'], effect = causeandeffect_data['effect_text'])
			causeandeffect.save()

			# # Set up many-to-many associations after saving the object
			if causeandeffect_data.has_key('question_id'):
				question = Question.objects.get(id=causeandeffect_data['question_id'])
				if question:
					causeandeffect.question_set.add(question)

			if causeandeffect_data.has_key('investigation_id'):
				investigation = Investigation.objects.get(id=causeandeffect_data['investigation_id'])
				if investigation:
					causeandeffect.investigations.add(investigation)

			# Serialize cause-and-effects in JSON format
			# i.e., https://docs.djangoproject.com/en/dev/topics/serialization/
			serialized_causeandeffects = serializers.serialize('json', [causeandeffect], fields=('cause', 'effect'))
			return HttpResponse(serialized_causeandeffects, mimetype="application/json")

		except KeyError:
			HttpResponseServerError("Malformed cause-and-effect data!")

		return HttpResponse(object)

	else:
		HttpResponseServerError("Not POST.  Must POST to this URL.")

@csrf_exempt
def causeandeffect_image_read(request, causeandeffect_id):
	if request.method == 'GET':
		try:
			causeandeffect = CauseAndEffect.objects.get(id=causeandeffect_id)
			#causeandeffect_images = CauseAndEffect.objects.get(id=causeandeffect_id).causeandeffect_set.all();
			causeandeffect_images = CauseAndEffectImage.objects.filter(causeandeffect_id=causeandeffect.id)
			#causeandeffect_images = CauseAndEffectImage.objects.filter(causeandeffect__id__exact=causeandeffect_id)
		except:
			raise Http404

		# Retreive request data
		format = request.GET['format'] if 'format' in request.GET else None

		if format == 'json':
			# Serialize questions in JSON format
			# i.e., https://docs.djangoproject.com/en/dev/topics/serialization/
			serialized_causeandeffects = serializers.serialize('json', causeandeffect_images)
			response = HttpResponse(serialized_causeandeffects, mimetype="application/json")
			response['Access-Control-Allow-Origin'] = '*'
			return response

	elif request.method == 'OPTIONS':
		# Enable CORS (Cross-Origin Resource Sharing)
		# http://enable-cors.org/#how-gae
		# - This must be added to headers to enable requests from origins other 
		#   than Google (i.e., wherever students host their websites).
		#self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		response = HttpResponse()
		response['Access-Control-Allow-Origin'] = '*'
		
		# Enable access to the DELETE HTTP request method cross-origin
		# http://www.w3.org/TR/cors/#introduction
		response['Access-Control-Max-Age'] = '3600'
		#response['Access-Control-Allow-Methods'] = 'DELETE'

@csrf_exempt
def investigation_create_api(request):
	if request.method == 'POST':

		investigation_json = request.body
		json_data = simplejson.loads(investigation_json)

		try:
			#data = json_data[0]
			investigation_data = json_data['investigation']

			# return HttpResponse(causeandeffect_json)

			investigation = Investigation() #(cause = investigation_data['cause_text'], effect = investigation_data['effect_text'])
			investigation.save()

			# Set up many-to-many associations after saving the object
			if investigation_data.has_key('question_id'):
				question = Question.objects.get(id=investigation_data['question_id'])
				if question:
					investigation.question_set.add(question)

			if investigation_data.has_key('causeandeffect_id'):
				causeandeffect = CauseAndEffect.objects.get(id=investigation_data['causeandeffect_id'])
				if causeandeffect:
					investigation.causeandeffect_set.add(causeandeffect)

			# Create steps
			for step in investigation_data['steps']:
				# step.text
				# step.number
				investigation_step = InvestigationStep()
				investigation_step.investigation = investigation
				investigation_step.number = step['number']
				investigation_step.text = step['text']
				investigation_step.save()

			# Serialize cause-and-effets in JSON format
			# i.e., https://docs.djangoproject.com/en/dev/topics/serialization/
			serialized_investigations = serializers.serialize('json', [investigation], fields=('cause_text', 'effect_text'))
			return HttpResponse(serialized_investigations, mimetype="application/json")

		except KeyError:
			HttpResponseServerError("Malformed cause-and-effect data!")

		return HttpResponse(object)

	else:
		HttpResponseServerError("Not POST.  Must POST to this URL.")

@csrf_exempt
def investigations_read_api(request):
	if request.method == 'GET':

		# Retreive request data
		format = request.GET['format'] if 'format' in request.GET else None
		question_id = request.GET['question_id'] if 'question_id' in request.GET else None
		causeandeffect_id = request.GET['causeandeffect_id'] if 'causeandeffect_id' in request.GET else None

		investigations = Investigation.objects.all()

		# Create association to question
		if question_id != None:
			investigations = investigations.filter(question__pk=question_id)

		# Create association to cause-and-effect
		if causeandeffect_id != None:
			investigations = investigations.filter(causeandeffect__pk=causeandeffect_id)

		# Serialize questions in JSON format
		# i.e., https://docs.djangoproject.com/en/dev/topics/serialization/
		serialized_investigations = serializers.serialize('json', investigations)
		response = HttpResponse(serialized_investigations, mimetype="application/json")
		response['Access-Control-Allow-Origin'] = '*'
		return response

	elif request.method == 'OPTIONS':
		# Enable CORS (Cross-Origin Resource Sharing)
		# http://enable-cors.org/#how-gae
		# - This must be added to headers to enable requests from origins other 
		#   than Google (i.e., wherever students host their websites).
		#self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		response = HttpResponse()
		response['Access-Control-Allow-Origin'] = '*'
		
		# Enable access to the DELETE HTTP request method cross-origin
		# http://www.w3.org/TR/cors/#introduction
		response['Access-Control-Max-Age'] = '3600'
		#response['Access-Control-Allow-Methods'] = 'DELETE'