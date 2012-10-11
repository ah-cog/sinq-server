from django.conf.urls import patterns, include, url

urlpatterns = patterns('sinq3.views',
	url(r'^$', 'home'), # /
	url(r'^questions/$', 'question_index'), # /questions/
	url(r'^questions/create/$', 'question_create'), # /questions/create/
	url(r'^questions_json/$', 'question_json'), # /questions/
	url(r'^questions_json/(?P<question_id>\d+)/$', 'question_id_json'), # /questions/{{ question.id }}/
	url(r'^questions_json/(?P<question_id>\d+)/images/$', 'question_id_image_json'), # /questions/{{ question.id }}/

	url(r'^questions/(?P<question_id>\d+)/$', 'question_view'), # /questions/{{ question.id }}/
	url(r'^questions/(?P<question_id>\d+)/edit/$', 'question_edit'), # /questions/{{ question.id }}/edit/

	url(r'^questions/(?P<question_id>\d+)/images/create/$', 'question_image_create'), # /questions/{{ question.id }}/pictures/create/
)