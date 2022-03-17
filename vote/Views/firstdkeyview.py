from tokenize import group
from django.shortcuts import render
from django.template import loaders
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
	context = {'pod':firstdel_groups.objects.all()}
	return render(request,"key/key.html",context )
         
def fkey_generator(request):
    if not request.user.is_authenticated:
      return redirect("/")
    podlength=len(pod_groups_members.objects.filter(member_status = 1))
    print(">>>>>>>>>>>",podlength)
    user = firstdel_groups.objects.filter(group_owner_id=request.user).order_by('group_owner_id')  
    
    if request.method=="POST":
        key=firstdel_groups()
        member=firstdel_groups_members()
        key.group_key=''.join(random.choices(string.digits, k=6))
        current_user=request.user          
        key.group_owner=current_user
        

        # print(key.group_owner.id)

        key.save()      
        member.member_status = 1
        #approval=member.approval_states
        member.group_id=key.id
        member.member_id=current_user.id
        member.save()   
        return HttpResponseRedirect(reverse("vote:fkey2",args=[key.id])) 
    if firstdel_groups_members.objects.filter(member_id=request.user.id).exists():
        return redirect("/fshow")
    return render(request,"key/firstdelkey.html",{'user':user,'is_key_generate':1,'s':0})



def fshow(request,id):
    elect_obj=firstdel_groups_members.objects.filter(member_id=request.user.id).values_list("elect_count",flat=True)[0]
    print("1010",elect_obj)
    count_obj = firstdel_groups_members.objects.filter(member_id=request.user.id).values_list("vote_count",flat=True)[0]
    print("counterrrr",count_obj)   
    currnt = firstdel_groups_members.objects.filter(member_id = request.user.id)
    hello = currnt.values_list("vote_given",flat=True)
    if firstdel_groups_members.objects.filter(member_id = request.user.id).exists():
        hell=hello[0]
    else:
        hell=0
       
    hello = currnt.values_list("elect_vote_given",flat=True)
    if firstdel_groups_members.objects.filter(member_id = request.user.id).exists():
        evote=hello[0]
    else:
        evote=0
   
    # print(evote)    
    devote = currnt.values_list("devote_given",flat=True)
    if firstdel_groups_members.objects.filter(member_id = request.user.id).exists():
        devotee=devote[0]
    else:
        devotee=0

    key1=firstdel_groups.objects.get(id=id)
    all=firstdel_groups.objects.filter(id=key1.id)
    users = firstdel_groups.objects.filter(id=key1.id) 
    if not request.user.is_authenticated:
      return redirect("/")
    user = firstdel_groups.objects.filter(group_owner_id=request.user)
    
    k=user.values_list('group_owner_id',flat=True)
    if firstdel_groups.objects.filter(group_owner_id=request.user).exists():
        owner_id=k[0]
    else:
        owner_id=0       
    approval_obj = firstdel_groups_members.objects.filter(group_id=key1)
    podlength=len(firstdel_groups_members.objects.filter(group_id=key1,member_status = 1))
    array=[]
    z=approval_obj
    for i in z:
        if i.member_status == 1:
            array.append(i)

        elif i.member_status == 0 and i.member_id == request.user.id and i.group_id == key1.id:
            break

        elif firstdel_groups_members.objects.filter(member_status=0,member_id=request.user.id,group_id = key1.id):
            break

        elif i.member_status == 0:
            array.append(i)
            break
    status=array[:12]
    if request.method=="POST" and "submit" in request.POST:
        if firstdel_groups_members.objects.filter(member_status=0,group_id=key1):
             firstdel_groups_members.objects.update(vote_given=0)
        member=firstdel_groups_members() 
        q = request.POST.get('submit')
        voteCount=F('vote_count')+1   
        member.vote_count=firstdel_groups_members.objects.filter(id=q).update(vote_count=voteCount)  
        member.vote_given=firstdel_groups_members.objects.filter(member_id=request.user.id).update(vote_given=1)  
        
        show=firstdel_groups_members.objects.filter(id=q)
        podlen=len(firstdel_groups_members.objects.filter(group_id=key1,member_status = 1))
        podLen=podlen/2
        length=podLen
        for i in show:
            print("Elect",i.vote_count)
        if i.vote_count > length:
            firstdel_groups_members.objects.filter(member_status =1,group_id=key1)
            firstdel_groups_members.objects.update(vote_given=0)
            member.pod_owner_id_id=firstdel_groups_members.objects.filter(id=q).update(member_status=1)   
        return redirect(request.path_info)   
    
    if request.method=="POST" and "devote" in request.POST:
        if firstdel_groups_members.objects.filter(member_status=0,group_id=key1):
             firstdel_groups_members.objects.update(vote_given=0)
        member=firstdel_groups_members() 
        q = request.POST.get('devote')
        print("q",q)
        voteCount=F('vote_count')-1   
        member.vote_count=firstdel_groups_members.objects.filter(id=q).update(vote_count=voteCount)  
        member.devote_given=firstdel_groups_members.objects.filter(member_id=request.user.id).update(devote_given=1)
        show=firstdel_groups_members.objects.filter(id=q)
        podlen=len(firstdel_groups_members.objects.filter(group_id=key1,member_status = 1))
        podLen=podlen/2
        length=podLen
        for i in show:
            print("Elect",i.vote_count)
        if i.vote_count < length:
            print(i.member.id)
            firstdel_groups_members.objects.filter(member_status =1,group_id=key1)
            print("true")
        #     #pod_groups_members.objects.update(vote_given=0)
        #     member.pod_owner_id_id=pod_groups_members.objects.filter(id=q).update(member_status=0)   
        return redirect(request.path_info)   
    
    if request.method=="POST" and "Delete" in request.POST:
        member=firstdel_groups_members()
        q = request.POST.get('Delete')
        member.count=firstdel_groups_members.objects.filter(id=q).delete()
        firstdel_groups_members.objects.filter(member_status =1).update(devote_given=0)
        firstdel_groups_members.objects.filter(member_status =1).update(vote_given=0)
        return redirect(request.path_info) 

    if request.method == "POST" and "hello" in request.POST:
        z =''.join(random.choices(string.digits, k=6))
        firstdel_groups.objects.filter(group_owner_id=request.user.id).update(group_key=z)
        return redirect(request.path_info) 
              
    

    if request.method=="POST" and "elect" in request.POST:
        member=firstdel_groups_members()
        mem=firstdel_groups()
        q = request.POST.get('elect')
        voteCount=F('elect_count')+1
        member.elect_count=firstdel_groups_members.objects.filter(id=q).update(elect_count=voteCount)  
        member.elect_vote_given=firstdel_groups_members.objects.filter(member_id=request.user.id).update(elect_vote_given=1)        
        podlen=len(firstdel_groups_members.objects.filter(group_id=key1,member_status = 1))
        podLen=podlen/2
        length=podLen
        # print("pod_length",length)
        show=firstdel_groups_members.objects.filter(id=q)
        for i in show:
             print("Elect",i.elect_count,i.group.group_owner_id)
        if i.elect_count > length:
            # print(i.member.id)
            mem.group_owner_id=firstdel_groups.objects.filter(group_owner=i.group.group_owner_id).update(group_owner=i.member.id)     
        return redirect(request.path_info)   
    return render(request,"key/firstdelkey.html",{'user':users,'key1':key1,'stat':status,'is_key_generate':0,'podlen':podlength,"owner_id":owner_id,'all':all,'votegive':hell,"evote":evote,'w':0,"devote":devotee,'count_obj':count_obj,'elect_obj':elect_obj}) 
 
    





    

