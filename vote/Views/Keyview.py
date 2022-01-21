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


def index(request):
	context = {'pod':pod.objects.all()}
	return render(request,"key/key.html",context )
         
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
    users = pod.objects.filter(id=key1.id)  
    context= user.objects.filter(id=key1.id)

    if request.method=="POST":
        key=pod()
        key.pod_key=''.join(random.choices(string.digits, k=6))

    return render(request,"key/key.html",{'context':context,'user':users,'key1':key1}) 

def show2(request,id):
    key2=pod.objects.get(id=id)
    print(key2.id)
    users = pod.objects.filter(id=key2.id)
    context=  user.objects.filter(id=id)
    if request.method=="POST":
        key=pod()
        key.pod_key=''.join(random.choices(string.digits, k=6))
        #return HttpResponseRedirect(reverse("vote:view",args=[key2.id]))  
    return render(request,"key/key.html",{'user':users,'context':context,'key2':key2}) 

