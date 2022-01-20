from logging import lastResort
from ssl import SSLSession
from django.shortcuts import render
from django.http import HttpResponse, request
from django.template import loader
import vote
from vote.models import *
from django.shortcuts import redirect
from django.contrib import messages
import random
import string
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect


         
def key_generator(request):
    
    user = pod.objects.filter(pod_owner_id_id=request.user).order_by('pod_owner_id_id')  
    
    #if request.session.has_key('pod_id'):
        
    if request.method=="POST":
        key=pod()
        member=pod_member()
        key.pod_key=''.join(random.choices(string.digits, k=6))
        current_user=request.user          
        key.pod_owner_id=current_user
        print(key.pod_owner_id.id)
        key.save()   

        #request.session['pod_id']=key.id
        member.pod_id_id=key.id
        member.member_id_id=current_user.id
        member.save()   
        return HttpResponseRedirect(reverse("vote:key2",args=[key.id])) 

    return render(request,"key/key.html",{'user':user})


def show(request,id):
    key1=pod.objects.get(id=id)
    user = pod.objects.filter(id=key1.id)
    print(user.query)
    
    context= pod_member.objects.filter(pod_id=key1)
    if request.method=="POST":
        key=pod()
        key.pod_key=''.join(random.choices(string.digits, k=6))

    print(context.query)

    return render(request,"key/key.html",{'context':context,'user':user,'key1':key1}) 
