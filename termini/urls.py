from django.conf.urls import patterns, url

urlpatterns = patterns('termini.views',
    url(r'^$', 'shift_week', name='shift_week'),
    url(r'^(?P<shift_id>\d+)/add-remove/$', 'shift_add_remove', name='shift_add_remove'),
)
