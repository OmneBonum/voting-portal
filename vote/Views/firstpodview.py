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

     
def fpodshow(request):  
     key2=firstdel_groups_members.objects.filter(member_id=request.user.id)
     print(key2)
     fpods=firstdel_groups.objects.filter(group_owner_id=request.user.id)
     k=fpods.values_list('group_owner_id',flat=True)
     values_obj=firstdel_groups.objects.count()
     user_obj=(values_obj)
     # print("k",k)
     if firstdel_groups.objects.filter(group_owner_id=request.user).exists():
        owner_id=k[0]
     else:
        owner_id=0

     print("fpods",fpods)

     if key2:
          print(key2)
          for i in key2:
               z=i.group_id
            
          current_user =request.user.id
          a = firstdel_groups_members.objects.filter(member_id=current_user).exists()
          
          return render(request,'pod/firsthome.html',{'keys':z,'a':a,'fpod':owner_id,'fkey':0,"value":user_obj})
     
     else:      
          current_user =request.user.id
          a = firstdel_groups_members.objects.filter(member_id=current_user).exists()
     return render(request,'pod/firsthome.html',{'a':a})


def fvalidate(request):
     if request.method =="POST":
          join=firstdel_groups_members()
         
          uname= request.POST.get('pod_keys')
          # print("uname",uname)
          if firstdel_groups.objects.filter(group_key=uname).exists()  :
               key1=firstdel_groups.objects.filter(group_key=uname)
               for i in key1:
                    z=i.id
                    # print('z',z)
                    
               # print(uname)
               current_user=request.user.id
               join.member_id=current_user
               join.group_id=z    
               join.member_status=0
               a=len(firstdel_groups_members.objects.filter(group_id=z))
               # print("a",a)
               #if a <= 11:
               join.save()
               return redirect('/fshow')
          else:
               messages.error(request,"Invalid key")
               return redirect('/fjoin') 
     return render(request,"pod/firstjoin.html")


