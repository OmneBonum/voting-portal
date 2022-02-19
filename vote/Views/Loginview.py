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
    con=pod_groups.objects.all()
    fcon=seconddel_groups.objects.all()
    context = sixthdel_groups.objects.all()
    s_key=seconddel_groups.objects.filter(group_owner_id=request.user.id)
    skey=s_key.values_list("group_key",flat=True).first()
    print("pod",skey)
    f_key=pod_groups.objects.filter(group_owner_id=request.user.id)
    pkey=f_key.values_list("group_key",flat=True).first()
    print("pod",pkey)
    pod_key=sixthdel_groups.objects.filter(group_owner_id=request.user.id)
    kkey=pod_key.values_list("group_key",flat=True).first()
    print("pod",kkey)
    if pod_groups.objects.filter(group_key=pkey):
      if firstdel_groups.objects.filter(group_owner_id=request.user.id):
        if seconddel_groups.objects.filter(group_owner_id=request.user.id):
          if thirddel_groups.objects.filter(group_owner_id=request.user.id): 
            if fourthdel_groups.objects.filter(group_owner_id=request.user.id): 
              if fifthdel_groups.objects.filter(group_owner_id=request.user.id):
                if sixthdel_groups.objects.filter(group_owner_id=request.user.id):
                  return render(request,"app/index.html",{'context':context,'kkey':kkey,'fcon':fcon,'pkey':skey,'z':0})  
                else:
                  return render(request,"app/index.html",{'context':context,'kkey':kkey,'fcon':fcon,'pkey':skey,'si':0})
              else:
                return render(request,"app/index.html",{'context':context,'kkey':kkey,'fcon':fcon,'pkey':skey,'fi':0})
            else:
              return render(request,"app/index.html",{'context':context,'kkey':kkey,'fcon':fcon,'pkey':skey,'fo':0})
          else:
            return render(request,"app/index.html",{'context':context,'kkey':kkey,'fcon':fcon,'pkey':skey,'th':0 }) 
        else:
          return render(request,"app/index.html",{'context':context,'kkey':kkey,'con':con,'pkey':pkey,'s':0}) 
      else:  
        return render(request,"app/index.html",{'context':context,'kkey':kkey,'con':con,'pkey':pkey,'f':0})  
    return render(request,"app/index.html",{'context':context,'kkey':kkey,'con':con,'pkey':pkey,'f': 0}) 

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