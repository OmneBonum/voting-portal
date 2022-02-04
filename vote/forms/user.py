from ast import Break
from django.forms import IntegerField, ModelForm
from django import forms
from vote.models import *


class AddCreateForm(ModelForm):
    district = forms.CharField(required = True,widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder':'Enter your District'
        }
    )) 

    
    email = forms.CharField(required = True,widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder':'Enter your Email address'
        }
    ))
    name = forms.CharField(label="Legal_name",required = True,widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder':'Enter your name',
        
        }
    ))

    registered = forms.BooleanField(label="I_am_a_registered_voter_in_this_district")
      
    
    
    eligible=forms.BooleanField(label="I believe i am eligible to vote in this district uder the name and address i will provide below and i intend to register as a voter within 30 days")

    
    password = forms.CharField(required = True,widget=forms.PasswordInput(
        attrs={
        'class':'form-control',
        'placeholder':'Enter your Password',
        }
    ))

    

    confirmation = forms.CharField(required = True,widget=forms.PasswordInput(
        attrs={
        'class':'form-control',
        'placeholder':'Confirm your Password',
        
        }
    ))

    address=forms.CharField(required=True,widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder':'Enter your address'
        
        }
    ))

    executed_on=forms.DateField(required = True,widget=forms.DateInput(
        attrs={
        'class':'form-control',
        'type': 'date',
        'placeholder':'Select date'
        }
    ))


    

    class Meta:
        model = user
        fields = ["district","name","registered","eligible","email","address","executed_on","password","confirmation"]