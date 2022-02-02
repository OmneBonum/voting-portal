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


    confirmation = forms.CharField(required = True,widget=forms.TextInput(
        attrs={
        'class':'form-control',
        
        }
    ))

    address=forms.CharField(required=True,widget=forms.TextInput(
        attrs={
        'class':'form-control',
        
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
        fields = ["name","district","email","password","confirmation","address","executed_on"]