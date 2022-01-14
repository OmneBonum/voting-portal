from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from vote.models import *
from django.contrib import messages



def index(request):
    context = {}
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render(context, request))

 
def create(request):
    if request.method == 'POST':
        signup=user()
        signup.district = request.POST.get('district')
        signup.voterid = request.POST.get('voterid')
        signup.name = request.POST.get('name')
        signup.email = request.POST.get('email')
        signup.password = request.POST.get('password')
        signup.confirmation = request.POST.get('confirmation')
        signup.save()
        return redirect("/signup")
    return render(request,"signup/create.html")

def update(request,id):
    users = user.objects.get(pk=id)
    print(users)
    if request.method=="POST":

        users.district = request.POST.get('district')
        users.voterid = request.POST.get('voterid')
        users.name = request.POST.get('name')
        users.email = request.POST.get('email')
        users.password = request.POST.get('password')
        users.confirmation = request.POST.get('confirmation')
        users.upload=request.POST.files("upload")
        users.save()
        return redirect('/login')
   
    return render(request,"signup/update.html",{'users':user})


