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


def spodshow(request):  
     key2=seconddel_groups_members.objects.filter(member_id=request.user.id)
     print(key2)
     
     fpods=seconddel_groups.objects.filter(group_owner_id=request.user.id)
     k=fpods.values_list('group_owner_id',flat=True)
     print("k",k)
     if seconddel_groups.objects.filter(group_owner_id=request.user).exists():
        owner_id=k[0]
     else:
        owner_id=0

     if key2:
          print(key2)
          for i in key2:
               z=i.group_id
               print("z id",z)
          
          print("asdf")
          # if pod_groups_members.objects.filter(member_status = 0,group_id=z):
          #      pod_groups_members.objects.update(vote_given=0)
          current_user =request.user.id
          a = seconddel_groups_members.objects.filter(member_id=current_user).exists()
          
          return render(request,'pod/shome.html',{'keys':z,'a':a,'spod':owner_id,'skey':0})
     
     else:      
          current_user =request.user.id
          a = seconddel_groups_members.objects.filter(member_id=current_user).exists()
     return render(request,'pod/shome.html',{'a':a})


def svalidate(request):
     if request.method =="POST":
          join=seconddel_groups_members()
         
          uname= request.POST.get('pod_keys')
          print("uname",uname)
          if seconddel_groups.objects.filter(group_key=uname).exists()  :
               key1=seconddel_groups.objects.filter(group_key=uname)
               for i in key1:
                    z=i.id
                    print('z',z)
                    
               print(uname)
               current_user=request.user.id
               join.member_id=current_user
               join.group_id=z    
               join.member_status=0
               a=len(seconddel_groups_members.objects.filter(group_id=z))
               print("a",a)
               #if a <= 11:
               join.save()
               return redirect('/sshow')
          else:
               messages.error(request,"Invalid key")
               return redirect('/sjoin') 
     return render(request,"pod/sjoin.html")

# def trying (request):
#      t=validate(request)
#      return HttpResponse("index.html")