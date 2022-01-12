from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . models import *


def index(request):
    context = {}
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render(context, request))



# def signup(request):
#     return HttpResponse(template.render(context, request))


# def login(request):
#     context = {}
#     template = loader.get_template('login.html')
#     return HttpResponse(template.render(context, request)) 


def help(request):
    context = {}
    template = loader.get_template('help.html')
    return HttpResponse(template.render(context, request))    