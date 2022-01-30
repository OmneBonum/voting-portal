from django.shortcuts import render
from django.http import HttpResponse, request
from django.template import loader
from vote.models import *
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
import random  
import string



def podshow(request):
     
     key1=pod_member.objects.filter(member_id_id=request.user.id)
     print(key1)
     if key1:
          print(key1)
          for i in key1:
               z=i.pod_id_id
          
          print("asdf")
          current_user =request.user.id
          a = pod_member.objects.filter(member_id_id=current_user).exists()
          return render(request,'pod/home.html',{'key1':z,'a':a})
     
     else:      
          current_user =request.user.id
          a = pod_member.objects.filter(member_id_id=current_user).exists()
     return render(request,'pod/home.html',{'a':a})


def validate(request):
     if request.method =="POST":
          join=pod_member()
     
          uname= request.POST.get('pod_key')

          if pod.objects.filter(pod_key=uname).exists():
               key1=pod.objects.filter(pod_key=uname)

          
               for i in key1:
                    z=i.id
                    print('z',z)
               #id=pod.objects.filter(pod_owner_id_id=18)
               print(uname)
               current_user=request.user.id
               join.member_id_id=current_user
               join.pod_id_id=z     
               join.approval_status=0
            
               join.save()
               
               return redirect('/show')
          else:
               messages.error(request,"Invalid Key")
               return redirect('/join')
     return render(request,"pod/join.html")






