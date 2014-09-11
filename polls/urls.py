from django.conf.urls import patterns, url
from polls import views as poll_view

urlpatterns = patterns('',
	url(r'^$', poll_view.index, name='index'),
	url(r'^(?P<question_id>\d+)/$', poll_view.detail, name='detail'),
	# ex: /polls/5/results/
	url(r'^(?P<question_id>\d+)/results/$', poll_view.results, name='results'),
	# ex: /polls/5/vote/
	url(r'^(?P<question_id>\d+)/vote/$', poll_view.vote, name='vote'),
	url(r'^list$', poll_view.product_list)
	)