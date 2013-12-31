from django.conf.urls import patterns, url
from play import views
from django.conf import settings
urlpatterns = patterns('',
    url(r'^home/', views.home, name='home'),
    url(r'^about/', views.about, name='about'),
    url(r'^music/', views.music, name='music'),

)

