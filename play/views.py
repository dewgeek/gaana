from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext

def home(request):
    return render(request, 'play/home.html')


def about(request):
    return render(request, 'play/about.html')
