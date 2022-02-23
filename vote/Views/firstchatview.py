from django.shortcuts import render, redirect
from vote.models import *
from django.http import HttpResponse, JsonResponse

# Create your views here.
# def home(request):
#     return render(request, 'chat/home.html')

def froom(request, froom):
    username = request.GET.get('username')
    # room_details = Room.objects.get(name=room)
    return render(request, 'chat/froom.html', {
        'username': username,
        # 'room': room,
        # 'room_details': room_details
    })

def fcheckview(request):
    # room = request.POST['room_name']
    #username = request.POST['username']

    # if pod_groups.objects.filter(group_owner_id=request.user.id).exists():
        if firstdel_groups.objects.filter(group_owner_id=request.user.id).exists():
            if seconddel_groups.objects.filter(group_owner_id=request.user.id).exists():
                if thirddel_groups.objects.filter(group_owner_id=request.user.id).exists():
                    if fourthdel_groups.objects.filter(group_owner_id=request.user.id).exists():
                        if fifthdel_groups.objects.filter(group_owner_id=request.user.id).exists():
                            if sixthdel_groups.objects.filter(group_owner_id=request.user.id).exists():
                                return redirect('/fcheckview')
                            else:
                                return redirect('/fcheckview')
                        else:
                            return redirect('/fcheckview')

                    else:
                        return redirect('/fcheckview')
                                       
                else:
                    return redirect('/fcheckview')

            else:   
                return redirect('/fcheckview')
    # return redirect('/fcheckview')
    # else:
    #     new_room = Room.objects.create(name=room)
    #     new_room.save()
    #     return redirect('/checkview')

def fsend(request):
    message = request.POST['message']   
    # key1=pod_groups_members.objects.filter(member_id=request.user.id)
  
    # if key1:
    #     print(key1) 
    #     for i in key1:
    #         z=i.group_id
    key2=firstdel_groups_members.objects.filter(member_id=request.user.id)
    
    if key2:
        print(key2) 
        for i in key2:
            z=i.group_id

    key3=seconddel_groups_members.objects.filter(member_id=request.user.id)
    
    if key3:
        print(key3) 
        for i in key3:
            z=i.group_id

    key4=thirddel_groups_members.objects.filter(member_id=request.user.id)
    
    if key4:
        print(key4) 
        for i in key4:
            z=i.group_id
          
    key5=fourthdel_groups_members.objects.filter(member_id=request.user.id)
    
    if key5:
        print(key5) 
        for i in key5:
            z=i.group_id

    key6=fifthdel_groups_members.objects.filter(member_id=request.user.id)
    
    if key6:
        print(key6) 
        for i in key6:
            z=i.group_id

    key7=sixthdel_groups_members.objects.filter(member_id=request.user.id)
    
    if key7:
        print(key7) 
        for i in key7:
            z=i.group_id
    new_message = firstMessage.objects.create(value=message, user=request.user.name,room=z)

    new_message.save()
    return HttpResponse('Message sent successfully')


def fgetMessages(request):
    #room_details = Room.objects.get(name=room)
    # key1=pod_groups_members.objects.filter(member_id=request.user.id) 

    # if key1:
    #     print(key1) 
    #     for i in key1:
    #         z=i.group_id
    key2=firstdel_groups_members.objects.filter(member_id=request.user.id)
    
   

    if key2:
        print(key2) 
        for i in key2:
            z=i.group_id
     
    key3=seconddel_groups_members.objects.filter(member_id=request.user.id)
    
    if key3:
        print(key3) 
        for i in key3:
            z=i.group_id
    
    key4=thirddel_groups_members.objects.filter(member_id=request.user.id)
    
    if key4:
        print(key4) 
        for i in key4:
            z=i.group_id
          
    key5=fourthdel_groups_members.objects.filter(member_id=request.user.id)
    
    if key5:
        print(key5) 
        for i in key5:
            z=i.group_id

    key6=fifthdel_groups_members.objects.filter(member_id=request.user.id)
    
    if key6:
        print(key6) 
        for i in key6:
            z=i.group_id

    key7=sixthdel_groups_members.objects.filter(member_id=request.user.id)
    
    if key7:
        print(key7) 
        for i in key7:
            z=i.group_id
    

    messages = firstMessage.objects.filter(room=z)#ll
    print("messages",messages)
    return JsonResponse({"messages":list(messages.values())})
