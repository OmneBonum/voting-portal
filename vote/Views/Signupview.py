from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from vote.models import *
from django.contrib import messages


def index(request):
    context = {}
    template = loader.get_template('app/index2.html')
    return HttpResponse(template.render(context, request))
    
def create(request):
    # user=User.objects.get(id=id)
    if request.method == 'POST':
        signup=user()
        signup.district = request.POST.get('district')
        signup.voterid = request.POST.get('voterid')
        signup.name = request.POST.get('name')
        signup.email = request.POST.get('email')
        signup.password = request.POST.get('password')
        signup.confirmation = request.POST.get('confirmation')
        signup.save()
        messages.success(request,'Insurance Added Successfully.')
        return redirect('/login')
    return render(request,"signup/create.html")

