from django.shortcuts import render
from django.http import HttpResponse, request
from django.template import loaders
from numpy import append, array
from rsa import verify
import vote
from vote.models import *
from django.shortcuts import redirect
from django.contrib import messages
import random
import string
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import F
from django.db.models import Count


def index(request):
	context = {'pod':pod.objects.all()}
	return render(request,"key/key.html",context )
         
def key_generator(request):
    user = pod.objects.filter(pod_owner_id_id=request.user).order_by('pod_owner_id_id')  
    if request.method=="POST":
        key=pod()
        member=pod_member()
        key.pod_key=''.join(random.choices(string.digits, k=6))
        current_user=request.user          
        key.pod_owner_id=current_user
        print(key.pod_owner_id.id)
        key.save()      
        member.pod_id_id=key.id
        member.member_id_id=current_user.id
        member.save()   
        return HttpResponseRedirect(reverse("vote:key2",args=[key.id])) 

    return render(request,"key/key.html",{'user':user})


def show(request,id):        
    key1=pod.objects.get(id=id)
    print("key1",key1)
    users = pod.objects.filter(id=key1.id)  
    context= pod_member.objects.filter(pod_id=key1)
    podlen=len(pod_member.objects.filter(pod_id=key1))
    podLen=podlen/2
    length=podLen
    countvalue = pod_member.objects.filter(pod_id=key1).values('count')
    if request.method=="POST":
        member=pod_member()
        q = request.POST.get('submit')
        z=q
        print("z",z)
    
        voteCount=F('count')+1   
        member.count=pod_member.objects.filter(id=q).update(count=voteCount)                 

    return render(request,"key/key.html",{'context':context,'user':users,'key1':key1,'podlen':length}) 


