
from django.shortcuts import render
from vote.models import *


def memberIndex(request):
    key1=pod_member.objects.filter(member_id_id=request.user.id)
    print(key1)
    if key1:
        print(key1)
        for i in key1:
            z=i.pod_id_id
            print("z",z)

    approval_obj = pod_member.objects.filter(approval_states = 1,pod_id=z).values_list("member_id",flat=True)
    user_obj = user.objects.filter(id__in=approval_obj)
    print(user_obj)

    if request.method == 'POST':
        member=pod_member()
        q = request.POST.get('text')
        print("q",q)
        member.text_states=pod_member.objects.filter(approval_states = 1,pod_id=z).update(text_states=q)

    return render(request,"pod/p.html",{'context':user_obj})




# def memberIndex(request):
#     if request.method == 'POST':
#         key1=pod_member.objects.filter(member_id_id=request.user.id)
#         print(key1)
#         if key1:
#             print(key1)
#             for i in key1:
#                 z=i.pod_id_id
#         approval_obj = pod_member.objects.filter(approval_states = 1,pod_id=z).values_list("member_id",flat=True)
#         user_obj = user.objects.filter(id__in=approval_obj)
#         print(user_obj)
#         return render(request,"pod/p.html",{'context':user_obj}