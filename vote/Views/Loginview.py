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
    f_key=pod_groups.objects.filter(group_owner_id=request.user.id)
    pkey=f_key.values_list("group_key",flat=True).first()
    template = loader.get_template('app/index.html')
    print("pod",pkey)
    
    if pod_groups.objects.filter(group_key=pkey):
      if firstdel_groups.objects.filter(group_owner_id=request.user.id):
        if seconddel_groups.objects.filter(group_owner_id=request.user.id):
          if thirddel_groups.objects.filter(group_owner_id=request.user.id): 
            if fourthdel_groups.objects.filter(group_owner_id=request.user.id): 
              if fifthdel_groups.objects.filter(group_owner_id=request.user.id):
                if sixthdel_groups.objects.filter(group_owner_id=request.user.id):
                  return render(request,"app/index.html",{'z':0})  
                else:
                  return render(request,"app/index.html",{'si':0})
              else:
                return render(request,"app/index.html",{'fi':0})
            else:
              return render(request,"app/index.html",{'fo':0})
          else:
            return render(request,"app/index.html",{'th':0 }) 
        else:
          return render(request,"app/index.html",{'s':0}) 
      else:  
        return render(request,"app/index.html",{'f':0})  
    return render(request,"app/index.html",{'f':0})  

def user_login(request):
    if request.method == "POST":
        uname= request.POST.get('email')
        print(uname)
        upass= request.POST.get('password')
        print(upass)      
        # print("hritik")
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
        #d
        if users is not None:
            login(request,users)

            pod_key=fifthdel_groups.objects.filter(group_owner_id=request.user.id)
            pkey=pod_key.values_list("group_key",flat=True).first()
            # print("pod",pkey)
            
            pod_key=sixthdel_groups.objects.filter(group_owner_id=request.user.id)
            kkey=pod_key.values_list("group_key",flat=True).first()
            print("pod",kkey)
            
            #group_keys=pkey[0]
            #print(group_keys[0])
            
            if firstdel_groups.objects.filter(group_owner_id=request.user.id) or firstdel_groups_members.objects.filter(member_id=request.user.id):
                if seconddel_groups.objects.filter(group_owner_id= request.user.id) or seconddel_groups_members.objects.filter(member_id=request.user.id)  :
                    if thirddel_groups.objects.filter(group_owner_id= request.user.id) or thirddel_groups_members.objects.filter(member_id=request.user.id):
                      if fourthdel_groups.objects.filter(group_owner_id= request.user.id) or fourthdel_groups_members.objects.filter(member_id=request.user.id):   
                        if fifthdel_groups.objects.filter(group_key= pkey) and fifthdel_groups_members.objects.filter(member_id=request.user.id):
                          if sixthdel_groups.objects.filter(group_owner_id= request.user.id) and sixthdel_groups_members.objects.filter(member_id=request.user.id):
                            return redirect('/sishow') 
                          else:
                            return redirect('/fishow') 
                        else:
                          return redirect('/foshow') 

                      else:  
                        return redirect('/tshow') 
                        
                    else: 
                      return redirect('/sshow') 
                    
                else:
                  return redirect('/fshow')  
         
            
            return redirect('/show')  

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


