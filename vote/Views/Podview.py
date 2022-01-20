from django.shortcuts import render
from django.http import HttpResponse, request
from django.template import loader
from vote.models import *
from django.shortcuts import redirect
from django.contrib import messages
import random
import string
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404



# def show(request):
#      a=pod.objects.all()
#      for i in a:
#           print(i.id)
#      if request.method == "POST":
#           current_user =request.user.id
#           print(current_user.id)
#           if pod_member.objects.filter(member_id_id=current_user).exists():
               
#                pass




#      return render(request,'pod/home.html')

def show(request):
     a=pod.objects.all()
     for i in a:
          b=i.id
     current_user =request.user.id
     print(current_user)
     a = pod_member.objects.filter(member_id_id=current_user).exists()

     return render(request,'pod/home.html',{'a':a})
 
    

def validate(request):
     context =pod.objects.all()
     for i in context:
          a=i.id
          print(a)
     if request.method =="POST":
          join=pod_member()
          # key=pod.objects.get(pod_owner_id_id=42)
          #print(key)
          uname= request.POST.get('pod_key')
          if pod.objects.filter(pod_key=uname).exists():
               print(uname)
               current_user=request.user.id
               join.member_id_id=current_user
               join.pod_id_id=a     
          
               join.save()
               return redirect('/pod')
          else:
               messages.error(request,"Invalid Key")
               return redirect('/join')
     return render(request,"pod/join.html",{'context':context})

