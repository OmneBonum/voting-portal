from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from vote.models import *
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from vote.forms.user import *
from django.db.models import F

# def index(request):
#     context = {}
#     template = loader.get_template('pod/p.html')
#     return HttpResponse(template.render(context, request))

def index(request):
    context = {'user_list':user.objects.all()}
    return render(request,"pod/p.html",context) 



def create(request):
    if request.method == 'POST':
        accountform = AddCreateForm(request.POST)
        if accountform.is_valid():
            new_user = accountform.save()
            new_user.set_password(
                accountform.cleaned_data.get('password')
                
            )
            if accountform.save():
                messages.success(request,'Account Added Successfully.')
                return redirect('/login')
        else:
            return render(request,"signup/create.html",{'form':accountform})

    form = AddCreateForm()
    return render(request,"signup/create.html",{'form':form})

def update(request,id):
    users = user.objects.get(id=id)
    print(users)
    if request.method=="POST":

        users.district = request.POST.get('district')
        users.voterid = request.POST.get('voterid')
        users.name = request.POST.get('name')
        users.email = request.POST.get('email')
        users.password = request.POST.get('password')
        users.confirmation = request.POST.get('confirmation')
        users.upload=request.FILES.get("upload")
        users.save()
        #return redirect('/login')
   
        return render(request,"create.html",{'users_list':users})


