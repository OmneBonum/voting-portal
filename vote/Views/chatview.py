from django.shortcuts import render, redirect
from vote.models import Room, Message, pod_groups, pod_groups_members
from django.http import HttpResponse, JsonResponse

# Create your views here.
# def home(request):
#     return render(request, 'chat/home.html')

def room(request, room):
    username = request.GET.get('username')
    # room_details = Room.objects.get(name=room)
    return render(request, 'chat/room.html', {
        'username': username,
        # 'room': room,
        # 'room_details': room_details
    })

def checkview(request):
    # room = request.POST['room_name']
    #username = request.POST['username']

    if pod_groups.objects.filter(group_owner_id=request.user.id).exists():
        return redirect('/checkview')
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/checkview')

def send(request):
    message = request.POST['message']   
    key1=pod_groups_members.objects.filter(member_id=request.user.id)
    if key1:
        print(key1) 
        for i in key1:
            z=i.group_id
     
    new_message = Message.objects.create(value=message, user=request.user,room=z)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request):
    #room_details = Room.objects.get(name=room)
    key1=pod_groups_members.objects.filter(member_id=request.user.id)
    if key1:
        print(key1) 
        for i in key1:
            z=i.group_id
     
          

    messages = Message.objects.filter(room=z)
    print("messages",messages)
    return JsonResponse({"messages":list(messages.values())})