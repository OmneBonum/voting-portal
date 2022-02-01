from django.shortcuts import render
from django.template import loaders
# from numpy import append, array
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
    user = pod.objects.filter(pod_owner_id=request.user).order_by('pod_owner_id')  
    if request.method=="POST":
        key=pod()
        member=pod_member()
        key.pod_key=''.join(random.choices(string.digits, k=6))
        current_user=request.user          
        key.pod_owner=current_user
        print(key.pod_owner.id)
        key.save()      
        member.member_status = 1
        #approval=member.approval_states
        member.pod_id=key.id
        member.member_id=current_user.id
        member.save()   
        return HttpResponseRedirect(reverse("vote:key2",args=[key.id])) 
    return render(request,"key/key.html",{'user':user})


def show(request,id):        
    key1=pod.objects.get(id=id)
    print("key1",key1)
    users = pod.objects.filter(id=key1.id) 
    user = pod.objects.filter(pod_owner_id=request.user)
    k=user.values_list('pod_owner_id',flat=True)
    if pod.objects.filter(pod_owner_id=request.user).exists():
        owner_id=k[0]
    else:
        owner_id=0       
    approval_obj = pod_member.objects.filter(pod_id=key1)
    podlength=len(pod_member.objects.filter(pod_id=key1,member_status = 1))
    print(podlength)
    array=[]
    z=approval_obj
    print("z",len(z))
    for i in z:
        if i.member_status == 1:
            array.append(i) 
        if i.member_status == 0:
            array.append(i)
            break
    
    status=array[:12]
    if request.method=="POST" and "submit" in request.POST:
        member=pod_member() 
        q = request.POST.get('submit')
        voteCount=F('pod_vote_count')+1   
        member.pod_vote_count=pod_member.objects.filter(id=q).update(pod_vote_count=voteCount)  
        member.pod_vote_given=pod_member.objects.filter(id=q).update(pod_vote_given=1)  
    
    
    if request.method=="POST" and "Delete" in request.POST:
        member=pod_member()
        q = request.POST.get('Delete')
        member.count=pod_member.objects.filter(id=q).delete()

    if request.method=="POST" and "elect" in request.POST:
        member=pod_member()
        mem=pod()
        q = request.POST.get('elect')
        z=q
        print("elect",z)
        voteCount=F('elect_count')+1
        member.elect_count=pod_member.objects.filter(id=z).update(elect_count=voteCount) 
        member.elect_vote_given=pod_member.objects.filter(id=z).update(elect_vote_given=1)        
        podlen=len(pod_member.objects.filter(pod_id=key1,member_status = 1))
        podLen=podlen/2
        length=podLen
        print("pod_length",length)
        show=pod_member.objects.filter(id=z)
        for i in show:
             print("Elect",i.elect_count,i.pod.pod_owner_id)
        if i.elect_count > length:
            print(i.member.id)
            mem.pod_owner_id_id=pod.objects.filter(pod_owner_id=i.pod.pod_owner_id).update(pod_owner_id=i.member.id) 
     
       
    return render(request,"key/key.html",{'user':users,'key1':key1,'stat':status,'podlen':podlength,"owner_id":owner_id}) 
 
    





    

