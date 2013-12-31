from django.conf.urls import patterns, url
from play import views

urlpatterns = patterns('',
    url(r'^home/', views.home, name='home'),
    url(r'^about/', views.about, name='about'),
    url(r'^music/', views.music, name='music'),

)
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
