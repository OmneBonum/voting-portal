from django.forms import IntegerField, ModelForm
from django import forms
from vote.models import *


class AddCreateForm(ModelForm):
    name = forms.CharField(required = True,widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder':'Enter your name'
        }
    ))
    
    email = forms.CharField(required = True,widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder':'Enter your address'
        }
    ))
    password = forms.CharField(required = True,widget=forms.PasswordInput(
        attrs={
        'class':'form-control'
        }
    ))

    district = forms.CharField(required = True,widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder':'Enter your District'
        }
    )) 


    confirmation = forms.IntegerField(required = True,widget=forms.TextInput(
        attrs={
        'class':'form-control',
        
        }
    ))


    class Meta:
        model = user
        fields = ["name","district","email","password","confirmation"]