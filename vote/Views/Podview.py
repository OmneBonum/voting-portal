from urllib import request
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
    
     all=pod_groups.objects.all()
     al=firstdel_groups.objects.all()
     pod_key=pod_groups.objects.filter(group_owner_id=request.user.id)
     f_key=firstdel_groups.objects.filter(group_owner_id=request.user.id)
     s_key=seconddel_groups.objects.filter(group_owner_id=request.user.id)
     pkey=pod_key.values_list("group_key",flat=True).first()
     print("pod",pkey)
     bkey=f_key.values_list("group_key",flat=True).first()
     print("bkey",bkey)
     skey=s_key.values_list("group_key",flat=True).first()
     print(skey)
     values_obj=pod_groups.objects.count()
     user_obj=(values_obj)
     print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,''''''''",user_obj)
     key1=pod_groups_members.objects.filter(member_id=request.user.id)
     
     fpods=pod_groups.objects.filter(group_owner_id=request.user.id)
     k=fpods.values_list('group_owner_id',flat=True)
     print("k",k)
     if not request.user.is_authenticated:
      return redirect("/")


     if pod_groups.objects.filter(group_owner_id=request.user).exists():
        owner_id=k[0]
     else:
        owner_id=0

    
     if key1:
          print(key1) 
          for i in key1:
               z=i.group_id
     
          
          print("asdf")
          current_user =request.user.id
          a = pod_groups_members.objects.filter(member_id=current_user).exists()
          # if request.user.is_authenticated:
          #      return redirect("sshow")
          return render(request,'pod/home.html',{'key1':z,'a':a,'fpod':owner_id,"fkey":0,'bkey':bkey,'pod':all,'al':al,'pkey':pkey,"value":user_obj})
     
     else:      
          current_user =request.user.id
          a = pod_groups_members.objects.filter(member_id=current_user).exists()
     return render(request,'pod/home.html',{'a':a,'fpods':fpods,'pkey':bkey,'pod':all,al:'al'})


def validate(request):
     if not request.user.is_authenticated:
        return redirect("/")
     if request.method =="POST":
          join=pod_groups_members()
         
          uname= request.POST.get('pod_key')
          if pod_groups.objects.filter(group_key=uname).exists()  :
               key1=pod_groups.objects.filter(group_key=uname)
               for i in key1:
                    z=i.id
                    print('z',z)
                    
               print(uname)
               current_user=request.user.id
               join.member_id=current_user
               join.group_id=z    
               join.member_status=0
               a=len(pod_groups_members.objects.filter(group_id=z))
               print("a",a)
               #if a <= 11:
               join.save()
               return redirect('/show')
          else:
               messages.error(request,"Invalid key")
               return redirect('/join') 
     return render(request,"pod/join.html")

# def trying (request):
#      t=validate(request)
#      return HttpResponse("index.html")
