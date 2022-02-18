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


def sixthpodshow(request):  
     key2=sixthdel_groups_members.objects.filter(member_id=request.user.id)
     print(key2)
     fpods=sixthdel_groups.objects.filter(group_owner_id=request.user.id)
     k=fpods.values_list('group_owner_id',flat=True)
     print("k",k)
     if sixthdel_groups.objects.filter(group_owner_id=request.user).exists():
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
          a = sixthdel_groups_members.objects.filter(member_id=current_user).exists()
          
          return render(request,'pod/sixthhome.html',{'keys':z,'a':a,'sipod':owner_id,'sikey':0})
     
     else:      
          current_user =request.user.id
          a = sixthdel_groups_members.objects.filter(member_id=current_user).exists()
     return render(request,'pod/sixthhome.html',{'a':a})


def sixthvalidate(request):
     if request.method =="POST":
          join=sixthdel_groups_members()
         
          uname= request.POST.get('pod_key')
          print("uname",uname)
          if sixthdel_groups.objects.filter(group_key=uname).exists()  :
               key1=sixthdel_groups.objects.filter(group_key=uname)
               for i in key1:
                    z=i.id
                    print('z',z)
                    
               print(uname)
               current_user=request.user.id
               join.member_id=current_user
               join.group_id=z    
               join.member_status=0
               a=len(sixthdel_groups_members.objects.filter(group_id=z))
               print("a",a)
               #if a <= 11:
               join.save()
               return redirect('/sishow')
          else:
               messages.error(request,"Invalid key")
               return redirect('/sijoin') 
     return render(request,"pod/sixthjoin.html")

# def trying (request):
#      t=validate(request)
#      return HttpResponse("index.html")
