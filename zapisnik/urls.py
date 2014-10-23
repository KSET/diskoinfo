from django.conf.urls import patterns, url

urlpatterns = patterns('zapisnik.views',
    url(r'^$', 'logentry_list', name='logentry_list'),
    url(r'^(?P<entry_id>\d+)/add-comment/$', 'add_comment', name='add_comment'),
    url(r'^(?P<entry_id>\d+)/(?P<comment_id>\d+)/del-comment/$', 'del_comment', name='del_comment')
    )
