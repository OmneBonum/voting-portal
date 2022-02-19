from contextlib import nullcontext
from tokenize import group
from django.forms import NullBooleanField
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from pymysql import NULL
from vote.models import *
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib import auth
from django.urls import reverse





def index(request):
    context = {}
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render(context, request))

def user_login(request):
    if request.method == "POST":
        uname= request.POST.get('email')
        print(uname)
        upass= request.POST.get('password')
        print(upass)      
        print("hritik")
        a=pod_groups.objects.all()
        for i in a: 
          b=i.id
        if request.method == "POST":
          current_user = request.user.id
          

        users = authenticate(username=uname,password=upass)
        print(users)    
        a=pod_groups.objects.filter(id=request.user.id)
        
        b=a.values_list("group_key",flat=True)
        print("group",b)
        
        if users is not None:
            login(request,users)

            pod_key=fifthdel_groups.objects.filter(group_owner_id=request.user.id)
            pkey=pod_key.values_list("group_key",flat=True).first()
            print("pod",pkey)
            
            #group_keys=pkey[0]
            #print(group_keys[0])
            
            if firstdel_groups.objects.filter(group_owner_id=request.user.id) and firstdel_groups_members.objects.filter(member_id=request.user.id):
                

                if seconddel_groups.objects.filter(group_owner_id= request.user.id) and seconddel_groups_members.objects.filter(member_id=request.user.id):
                    if thirddel_groups.objects.filter(group_owner_id= request.user.id) and thirddel_groups_members.objects.filter(member_id=request.user.id):
                      if fourthdel_groups.objects.filter(group_owner_id= request.user.id) and fourthdel_groups_members.objects.filter(member_id=request.user.id):  
                        
                        if fifthdel_groups.objects.filter(group_key= pkey) and fifthdel_groups_members.objects.filter(member_id=request.user.id):
                          return redirect('/fishow') 
                        else:
                          return redirect('/foshow') 

                      else:  
                        return redirect('/tshow') 
                        # else:
                        #     return redirect('/foshow')
                    else: 
                      return redirect('/sshow') 
                    # else:
                    #     return redirect('/tshow')

                        # return redirect('/tshow')
                else:
                  return redirect('/fshow')  
            # if seconddel_groups.objects.filter(group_key=bkey) and seconddel_groups_members.objects.filter(member_id=request.user.id):
            #    return redirect('/sshow') 
            
            # elif seconddel_groups.objects.filter(group_owner_id=request.user.id) and  thirddel_groups.objects.filter(group_owner_id=request.user.id):
            #    return redirect('/tshow') 
            
            return redirect('/show')
          
        # if firstdel_groups.objects.filter(group_owner_id=request.user.id) and user is not None:
        #   return redirect('/fshow')
       
        

        else:
          messages.error(request,"Invalid Credential")
          return redirect('/login')
              
    return render(request,"login.html")

def userLogout(request):
  auth.logout(request)
  return redirect('/login')


def help(request):
    context = {}
    template = loader.get_template('help.html')
    return HttpResponse(template.render(context, request))    


#and seconddel_groups_members.objects.filter(member_id=request.user.id)