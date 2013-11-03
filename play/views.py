from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
import fbconsole
import re
import time
import sys
from google import search
from random import choice
import webbrowser

def home(request):
    return render(request, 'play/home.html')


def about(request):
    return render(request, 'play/about.html')

def fb(request):

    fbconsole.AUTH_SCOPE = ['user_likes','publish_checkins' ]
    fbconsole.authenticate()
    music = fbconsole.fql("SELECT music FROM user  WHERE uid=me()")
    fbconsole.logout()

    music_list = music[0].values()
    for name in music_list:	#fetch music names
        music_name = (choice(name.split(','))).encode('utf-8')
        
    for url in search('%s gaana' %music_name, stop=1):
        if re.search(ur'http://gaana.com', url, re.UNICODE):
            webbrowser.open_new(url)
            break
        else:
            return HttpResponseRedirect('/play/error') 
    
    return render(request, 'play/over.html')
          


