from django.conf.urls import patterns, include, url

urlpatterns = patterns('sinq3.views',
	url(r'^$', 'home'), # /
	url(r'^questions/$', 'question_index'), # /questions/
	url(r'^questions/create/$', 'question_create'), # /questions/create/
	url(r'^questions/(?P<question_id>\d+)/images/$', 'question_image_read'), # /questions/{{ question.id }}/

	url(r'^questions/(?P<question_id>\d+)/$', 'question_read'), # /questions/{{ question.id }}/
	url(r'^questions/(?P<question_id>\d+)/edit/$', 'question_edit'), # /questions/{{ question.id }}/edit/

	url(r'^questions/(?P<question_id>\d+)/images/create/$', 'question_image_create'), # /questions/{{ question.id }}/pictures/create/

	url(r'^api/questions/create/$', 'question_create_api'), # /questions/create/
	url(r'^api/questions/(?P<question_id>\d+)/images/create/$', 'question_image_create_api'), # /questions/{{ question.id }}/pictures/create/

	# /questions/33/?format=json
)