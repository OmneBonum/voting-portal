from django.shortcuts import render
from vote.models import *

def memberIndex(request):
    key1=pod_groups_members.objects.filter(member_id=request.user.id)
    print(key1)
    if key1:
        print(key1)
        for i in key1:
            z=i.group_id
            print("z",z)

    approval_obj = pod_groups_members.objects.filter(member_status = 1,group_id=z).values_list("member",flat=True)
    
    user_obj = user.objects.filter(id__in=approval_obj)
    print(user_obj)
    if request.method == 'POST':
        member=pod_groups_members()
        q = request.POST.get('text')
        print(q)
    
        member.text_status=pod_groups_members.objects.filter(member_status=1,group_id=z).update(member_comment=q)
    return render(request,"pod/data.html",{'context':user_obj})


