from django.shortcuts import render
from vote.models import *


def memberIndex(request):
    key1=pod_member.objects.filter(member_id=request.user.id)
    print(key1)
    if key1:
        print(key1)
        for i in key1:
            z=i.pod_id
            print("z",z)

    approval_obj = pod_member.objects.filter(member_status = 1,pod_id=z).values_list("member",flat=True)
    
    user_obj = user.objects.filter(id__in=approval_obj)
    print(user_obj)
    if request.method == 'POST':
        member=pod_member()
        q = request.POST.get('text')
        print(q)
    
        member.text_status=pod_member.objects.filter(member_status=1,pod_id=z).update(member_comment=q)
    return render(request,"pod/data.html",{'context':user_obj})


# def show(request,id):
#     key1=pod.objects.get(id=id)
#     user = pod.objects.filter(pod_owner_id_id=request.user)
#     print(user)
#     podlength=len(pod_member.objects.filter(pod_id=key1))
#     print("podlength",podlength)   
#     if user:
#         for i in user:
#             pod_obj=i.pod_owner_id_id
#         key1=pod.objects.get(id=id)
#         print("key1",key1)
#         users = pod.objects.filter(id=key1.id)
#         podlengt=len(pod_member.objects.filter(pod_id=key1))
#         approval_obj = pod_member.objects.filter(pod_id=key1)
#         array=[]
#         z=approval_obj
#         for i in z:
#             print("i",i.approval_status)
#             if i.approval_status == 1 :
#                 array.append(i)
#             if i.approval_status == 0 :
#                 array.append(i)
#                 break
#         status=array
#         if request.method=="POST" and "submit" in request.POST:
#             member=pod_member()
#             q = request.POST.get('submit')
#             z=q
#             print("z",z)

#             voteCount=F('count')+1
#             member.count=pod_member.objects.filter(id=q).update(count=voteCount)
#             podlen=len(pod_member.objects.filter(pod_id=key1,approval_status=1))/2
#             print(podlen)
#             show=pod_member.objects.filter(id=q)
#             for i in show:
#                 print(i.count)
#             if i.count > podlen:
#                 member.approval_status=pod_member.objects.filter(id=q).update(approval_status=1)
                
#         if request.method=="POST" and "devote" in request.POST:
#             member=pod_member()
#             q = request.POST.get('devote')
#             z=q
#             print("z",z)
#             voteless=F('count')-1
#             podlen=len(pod_member.objects.filter(pod_id=key1,approval_status=1))/2
#             print(podlen)
#             member.count=pod_member.objects.filter(id=q).update(count=voteless)

            
#         if request.method=="POST" and "elect" in request.POST:
#             member=pod_member()
#             mem=pod()
#             q = request.POST.get('elect')
#             z=q
#             print("z",z)
#             vote=F('Elect_count')+1
#             podleng=len(pod_member.objects.filter(pod_id=key1,approval_status=1))/2
#             print(podleng)
#             member.Elect_count=pod_member.objects.filter(id=q).update(Elect_count=vote)
#             show=pod_member.objects.filter(id=q)
#             podleng=len(pod_member.objects.filter(pod_id=key1,approval_status=1))/2
#             print(podleng)
#             for i in show:
#                 print(i.count)
#             if i.count > podleng:    
#                 mem.pod_owner_id_id=pod.objects.filter(pod_owner_id_id=request.user).update(pod_owner_id_id=4) 
#                 #mem.pod_owner_id_id=pod.objects.filter(pod_owner_id_id=request.user).update(pod_owner_id_id=1)
#         return render(request,"key/key.html",{'user':users,'key1':key1,'stat':status,'pod_obj':pod_obj,"podlen":podlength})
#     else:
#         key1=pod.objects.get(id=id)
#         users = pod.objects.filter(id=key1.id)
#         podlength=len(pod_member.objects.filter(pod_id=key1))
#         approval_obj = pod_member.objects.filter(pod_id=key1)
#         array=[]
#         z=approval_obj
#         for i in z:
#             print("i",i.approval_status)
#             if i.approval_status == 1:
#                 array.append(i)
#             if i.approval_status == 0:
#                 array.append(i)
#                 break
#         status=array
#         if request.method=="POST" and "submit" in request.POST:
#             member=pod_member()
#             q = request.POST.get('submit')
#             z=q
#             print("z",z)

#             voteCount=F('count')+1
#             member.count=pod_member.objects.filter(id=q).update(count=voteCount)
#             podlen=len(pod_member.objects.filter(pod_id=key1,approval_status=1))/2
#             print(podlen)
#             show=pod_member.objects.filter(id=q)
#             for i in show:
#                 print(i.count)
#             if i.count > podlen:
#                 member.approval_status=pod_member.objects.filter(id=q).update(approval_status=1)
#         if request.method=="POST" and "devote" in request.POST:
#             member=pod_member()
#             q = request.POST.get('devote')
#             z=q
#             print("z",z)
#             voteless=F('count')-1
#             podlen=len(pod_member.objects.filter(pod_id=key1,approval_status=1))/2
#             print(podlen)
#             member.count=pod_member.objects.filter(id=q).update(count=voteless)

            
#         if request.method=="POST" and "elect" in request.POST:
#             member=pod_member()
#             mem=pod()
#             q = request.POST.get('elect')
#             z=q
#             print("z",z)
#             vote=F('Elect_count')+1
#             podleng=len(pod_member.objects.filter(pod_id=key1,approval_status=1))/2
#             print(podleng)
#             member.Elect_count=pod_member.objects.filter(id=q).update(Elect_count=vote)
#             show=pod_member.objects.filter(id=q)
#             podleng=len(pod_member.objects.filter(pod_id=key1,approval_status=1))/2
#             print(podleng)
#             for i in show:
#                 print(i.count)
#             if i.count > podleng:    
#                 mem.pod_owner_id_id=pod.objects.filter(pod_owner_id_id=request.user).update(pod_owner_id_id=4)
#             return render(request,"key/key.html",{'user':users,'key1':key1,'stat':status,'podlen':podlength})

