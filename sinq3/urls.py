from django.conf.urls import patterns, include, url

urlpatterns = patterns('sinq3.views',
	url(r'^$', 'home'), # /

	url(r'^causeandeffects/$', 'causeandeffects_index'), # /causeandeffects/
	url(r'^causeandeffects/(?P<causeandeffect_id>\d+)/images/$', 'causeandeffect_image_read'), # /causeandeffects/{{ causeandeffect.id }}/

	url(r'^questions/$', 'question_index'), # /questions/
	url(r'^questions/create/$', 'question_create'), # /questions/create/
	url(r'^questions/(?P<question_id>\d+)/images/$', 'question_image_read'), # /questions/{{ question.id }}/

	url(r'^questions/(?P<question_id>\d+)/$', 'question_read'), # /questions/{{ question.id }}/
	url(r'^questions/(?P<question_id>\d+)/edit/$', 'question_edit'), # /questions/{{ question.id }}/edit/

	url(r'^questions/(?P<question_id>\d+)/images/create/$', 'question_image_create'), # /questions/{{ question.id }}/images/create/


	# RESTful HTTP API

	url(r'^api/questions/$', 'questions_read_api'), # /api/questions/
	url(r'^api/questions/create/$', 'question_create_api'), # /api/questions/create/
	url(r'^api/questions/(?P<question_id>\d+)/images/$', 'question_image_read_api'), # /api/questions/?format=json
	url(r'^api/questions/(?P<question_id>\d+)/images/create/$', 'question_image_create_api'), # /questions/{{ question.id }}/images/create/

	url(r'^api/causeandeffects/$', 'causeandeffects_read_api'), # /api/causeandeffects/
	url(r'^api/causeandeffects/(?P<causeandeffect_id>\d+)/$', 'causeandeffect_read_api'), # /causeandeffects/{{ causeandeffect.id }}/
	url(r'^api/causeandeffects/create/$', 'causeandeffect_create_api'), # /causeandeffects/create/
	url(r'^api/causeandeffects/(?P<causeandeffect_id>\d+)/images/$', 'causeandeffect_image_read_api'), # /causeandeffects/{{ causeandeffect.id }}/
	url(r'^api/causeandeffects/(?P<causeandeffect_id>\d+)/images/create/$', 'causeandeffect_image_create_api'), # /causeandeffects/{{ causeandeffect.id }}/images/create/

	url(r'^api/investigations/$', 'investigations_read_api'), # /api/investigations/
	url(r'^api/investigations/create/$', 'investigation_create_api'), # /investigations/create/
	url(r'^api/investigations/(?P<investigation_id>\d+)/steps/$', 'investigation_step_read_api'), # /investigations/{{ investigation.id }}/steps/
	url(r'^api/investigations/(?P<investigation_id>\d+)/steps/create/$', 'investigation_step_create_api'), # /investigations/{{ investigation.id }}/steps/create/
	url(r'^api/investigations/(?P<investigation_id>\d+)/steps/(?P<steps_id>\d+)/images/create/$', 'investigation_step_image_create_api'), # /investigations/{{ investigation.id }}/steps/{{ step.id }}/images/create/

	# /questions/33/?format=json
)