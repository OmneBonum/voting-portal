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
	context = {'pod':pod_groups.objects.all()}
	return render(request,"key/key.html",context )
         
def key_generator(request):
    user = pod_groups.objects.filter(group_owner_id=request.user).order_by('group_owner_id')  
    
    if request.method=="POST":
        key=pod_groups()
        member=pod_groups_members()
        key.group_key=''.join(random.choices(string.digits, k=6))
        current_user=request.user          
        key.group_owner=current_user
        print(key.group_owner.id)
        key.save()      
        member.member_status = 1
        #approval=member.approval_states
        member.group_id=key.id
        member.member_id=current_user.id
        member.save()   
        return HttpResponseRedirect(reverse("vote:key2",args=[key.id])) 
    return render(request,"key/key.html",{'user':user})


def show(request,id):   
    currnt = pod_groups_members.objects.filter(member_id = request.user.id)
    # print("dskdksdhkshbd",currnt)
    hello = currnt.values_list("vote_given",flat=True)
    hell=hello[0]     
    print("hell",hell)
    hello = currnt.values_list("elect_vote_given",flat=True)
    evote=hello[0]
    print(evote)

    key1=pod_groups.objects.get(id=id)
    print("key1",key1)
    all=pod_groups.objects.filter(id=key1.id)
    users = pod_groups.objects.filter(id=key1.id) 
    user = pod_groups.objects.filter(group_owner_id=request.user)
    k=user.values_list('group_owner_id',flat=True)
    if pod_groups.objects.filter(group_owner_id=request.user).exists():
        owner_id=k[0]
    else:
        owner_id=0       
    approval_obj = pod_groups_members.objects.filter(group_id=key1)
    podlength=len(pod_groups_members.objects.filter(group_id=key1,member_status = 1))
    print(podlength)
    array=[]
    z=approval_obj
    print("z",len(z))
    for i in z:
        if i.member_status == 1:
            array.append(i) 
        if i.member_status == 0 and i.member_id == request.user.id:
            break
        if i.member_status == 0:
            array.append(i)
            break
    
    status=array[:12]
    if request.method=="POST" and "submit" in request.POST:
        member=pod_groups_members() 
        q = request.POST.get('submit')
        voteCount=F('vote_count')+1   
        member.vote_count=pod_groups_members.objects.filter(id=q).update(vote_count=voteCount)  
        member.vote_given=pod_groups_members.objects.filter(member_id=request.user.id).update(vote_given=1)  
        
        show=pod_groups_members.objects.filter(id=q)
        podlen=len(pod_groups_members.objects.filter(group_id=key1,member_status = 1))
        podLen=podlen/2
        length=podLen
        for i in show:
            print("Elect",i.vote_count)
        if i.vote_count > length:
            print(i.member.id)
            member.pod_owner_id_id=pod_groups_members.objects.filter(id=q).update(member_status=1) 
           

    
    if request.method=="POST" and "Delete" in request.POST:
        member=pod_groups_members()
        q = request.POST.get('Delete')
        member.count=pod_groups_members.objects.filter(id=q).delete()
    

    if request.method=="POST" and "elect" in request.POST:
        member=pod_groups_members()
        mem=pod_groups()
        q = request.POST.get('elect')
        voteCount=F('elect_count')+1
        member.elect_count=pod_groups_members.objects.filter(id=q).update(elect_count=voteCount) 
        member.elect_vote_given=pod_groups_members.objects.filter(member_id=request.user.id).update(elect_vote_given=1)        
        podlen=len(pod_groups_members.objects.filter(group_id=key1,member_status = 1))
        podLen=podlen/2
        length=podLen
        print("pod_length",length)
        show=pod_groups_members.objects.filter(id=q)
        for i in show:
             print("Elect",i.elect_count,i.group.group_owner_id)
        if i.elect_count > length:
            print(i.member.id)
            mem.group_owner_id=pod_groups.objects.filter(group_owner=i.group.group_owner_id).update(group_owner=i.member.id)     
    return render(request,"key/key.html",{'user':users,'key1':key1,'stat':status,'podlen':podlength,"owner_id":owner_id,'all':all,'votegive':hell,"evote":evote}) 
 
    





    
