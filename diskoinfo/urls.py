from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
from filebrowser.sites import site
from django.contrib.auth import views as auth_views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url=reverse_lazy('zapisnik:logentry_list'))),
    url(r'^zapisnik/', include('zapisnik.urls', namespace='zapisnik', app_name='zapisnik')),
    url(r'^termini/', include('termini.urls', namespace='termini', app_name='termini')),

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^changepwd/$', auth_views.password_change, name='changepwd'),
    url(r'^changepwd/done/$', auth_views.password_change_done, name='password_change_done'),
)

# staticfiles_urlpatterns() returns only if DEBUG, static also
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
