from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'principal.views.index'),
    url(r'^agregar/$', 'principal.views.agregar_evento'),
    url(r'^evento/(?P<id>\d)$', 'principal.views.evento'),
)
