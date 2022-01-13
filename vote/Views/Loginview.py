from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from vote.models import *
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import redirect
from django.contrib import messages



def index(request):
    context = {}
    template = loader.get_template('app/index2.html')
    return HttpResponse(template.render(context, request))

def login(request):
    if request.method == "POST":
        uname= request.POST.get('email')
        print(uname)
        upass= request.POST.get('password')
        print(upass)
        user = authenticate(username=uname,password=upass)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('/')

        else:
            messages.error(request,"Invalid Credential")
            

    return render(request,"login.html")