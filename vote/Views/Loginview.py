from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from vote.models import *
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib import auth




def index(request):
    context = {}
    template = loader.get_template('app/index.html')
    #print("asdfsgf",pod.pod_owner_id.get_object)
    # a=pod_member.objects.all()
    # for i in a:
    #   print(i.id,i.member_id.name,i.member_id.district)

    # print(1234,a)
    return HttpResponse(template.render(context, request))

def user_login(request):
    if request.method == "POST":
        uname= request.POST.get('email')
        print(uname)
        upass= request.POST.get('password')
        print(upass)
        a=pod.objects.all()
        for i in a: 
          b=i.id
        if request.method == "POST":
          current_user = request.user.id

        
        #i  f pod_member.objects.filter(member_id_id=current_user).exists():
            #request.session['pod_id']=b
    
        user = authenticate(username=uname,password=upass)
        print(user) 
        if user is not None:
          login(request,user)
          return redirect('/show')

        else:
          messages.error(request,"Invalid Credential")
          return redirect('/login')
              
    return render(request,"login.html")

def userLogout(request):
  auth.logout(request)
  return redirect('/login')