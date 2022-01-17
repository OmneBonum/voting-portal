import imp
from django.shortcuts import render
from django.http import HttpResponse, request
from django.template import loader
from vote.models import *
from django.shortcuts import redirect
from django.contrib import messages
import random
import string


# def show(request):
#      context = {}
#      template = loader.get_template('key/key.html')
#      return HttpResponse(template.render(context, request))

def key_generator(request):
     if request.method=="POST":
          key=pod()
          key.pod_key=''.join(random.choices(string.digits, k=6))
          key.pod_owner_id=request.user
          print(key.pod_owner_id)
          #key.pod_key= random(100000, 999999)
          key.save()
          return redirect("/")
     return render(request,"key/key.html")


