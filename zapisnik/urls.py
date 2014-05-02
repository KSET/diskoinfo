from django.conf.urls import patterns, url

urlpatterns = patterns('zapisnik.views',
    url(r'^$', 'logentry_list', name='logentry_list'),
    # url(r'^(?P<cv_id>\d+)/$', 'cv_detail', name='cv_detail'),
)
