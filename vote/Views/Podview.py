from django.shortcuts import render
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
     key1=pod_member.objects.filter(member_id=request.user.id)
     print(key1)
     if key1:
          print(key1)
          for i in key1:
               z=i.pod_id
          
          print("asdf")
          current_user =request.user.id
          a = pod_member.objects.filter(member_id=current_user).exists()
          return render(request,'pod/home.html',{'key1':z,'a':a})
     
     else:      
          current_user =request.user.id
          a = pod_member.objects.filter(member_id=current_user).exists()
     return render(request,'pod/home.html',{'a':a})


def validate(request):
     if request.method =="POST":
          join=pod_member()
         
          uname= request.POST.get('pod_key')
          if pod.objects.filter(pod_key=uname).exists()  :
               key1=pod.objects.filter(pod_key=uname)
               for i in key1:
                    z=i.id
                    print('z',z)
                    
               print(uname)
               current_user=request.user.id
               join.member_id=current_user
               join.pod_id=z    
               join.member_status=0
               a=len(pod_member.objects.filter(pod_id=z))
               print("a",a)
               if a <= 11:
                    join.save()
                    return redirect('/show')
               else:
                    
                    messages.error(request,"pod entries close")
                    return redirect('/join') 
     return render(request,"pod/join.html")






