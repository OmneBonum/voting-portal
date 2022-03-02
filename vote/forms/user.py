from ast import Break
from django.forms import IntegerField, ModelForm
from django import forms
from localflavor.us.forms import USStateField
from vote.models import *


FRUIT_CHOICES= [
    ('I_am_a_registered_voter_in_this_district', 'I_am_a_registered_voter_in_this_district'),
    ('I believe i am eligible to vote in this district uder the name and address i will provide below and i intend to register as a voter within 30 days','I believe i am eligible to vote in this district uder the name and address i will provide below and i intend to register as a voter within 30 days')
    ]



class AddCreateForm(ModelForm):
    
    # district = forms.CharField(required = True,widget=forms.TextInput(
    #     attrs={
    #     'class':'form-control',
    #     'placeholder':'Enter your District'
    #     }
    # )) 
    
    district= USStateField()
    
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

    
    registered= forms.BooleanField( widget=forms.RadioSelect(choices=FRUIT_CHOICES))
      
    
    
    # eligible= forms.BooleanField(label="", widget=forms.RadioSelect(choices=FRUIT_CHOICES))
    
    password = forms.CharField(required = True,widget=forms.PasswordInput(
        attrs={
        'class':'form-control',
        'placeholder':'Enter your Password',
        }
    ))

    

    confirmation = forms.CharField(label="Confirm_Password",required = True,widget=forms.PasswordInput(
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
        fields = ["district","name","registered","email","address","executed_on","password","confirmation"]

    def clean(self):
        cleaned_data = super(AddCreateForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirmation")

        if password != confirm_password:
             self.add_error("confirmation", forms.ValidationError("password and confirm_password does not match") 
            # raise forms.ValidationError(
            #     "password and confirm_password does not match"
            )  
       