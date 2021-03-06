from ast import Break
from cProfile import label
from multiprocessing.sharedctypes import Value

from django.forms import HiddenInput, IntegerField, ModelForm
from django import forms
from localflavor.us.forms import USStateField
from vote.models import *



FRUIT_CHOICES= [
    ('I am legally registered to vote in this US congressional district.'  ,  'I am legally registered to vote in this US congressional district.' ),
    ('I believe i am eligible to vote in this district under the name and address i will provide below and i intend to register as a voter within 30 days.','I believe i am eligible to vote in this district under the name and address i will provide below and i intend to register as a voter within 30 days.')
    ]



class AddCreateForm(ModelForm):
    
    district = forms.CharField(required = True,widget=forms.TextInput(
        attrs={
        'type':"text", 'maxlength':'4',
        'class':'user',
        'placeholder':'Enter your District',
        
        
        }
    )) 
    
    # district= USStateField()
    
    email = forms.CharField(required = True,widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder':'Enter your Email address'
        }
    ))
    Legal_name = forms.CharField(label="Legal Name",required = True,widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder':'Enter your name',
        
        }
    ))

    
    Registration_Status= forms.BooleanField(label="Registration Status", widget=forms.RadioSelect(choices=FRUIT_CHOICES))
      
    
    
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

    address=forms.CharField(required=True,widget=forms.Textarea(
        
        attrs={
        "rows":0, "cols":10,  
        'class':'form-control',
        'placeholder':'Enter your address'
        
        }
    ))

    # executed_on=forms.DateField(required = True,widget=forms.DateInput(
    #     attrs={
    #     'class':'form-control',
    #     'type': 'date',
    #     'placeholder':'Select date'
    #     }
    # ))


    

    class Meta:
        model = user
        fields = ["district","Legal_name","Registration_Status","email","address","password","confirmation"]

    def clean(self):
        cleaned_data = super(AddCreateForm, self).clean()
        password = cleaned_data.get("password")
        district = cleaned_data.get("district")
        if district is None:
            print("111111111111111  ")
            district = "hello"
        else:
            print("",district.upper())
            a=district.upper()
            listuser = ["AL01","AL02","AL03","AL04","AL05","AL06","AL07","AK01","AZ01","AZ02","AZ03","AZ04","AZ05","AZ06","AZ07","AZ08","AZ09","AR01","AR02","AR03","AR04","CA01","CA02","CA03","CA04","CA05","CA06","CA07","CA08","CA09","CA10","CA11","CA12","CA13","CA14","CA15","CA16","CA17","CA18","CA19","CA20","CA21","CA22","CA23","CA24","CA25","CA26","CA27","CA28","CA29","CA30","CA31","CA32","CA33","CA34","CA35","CA36","CA37","CA38","CA39","CA40","CA41","CA42","CA43","CA44","CA45","CA46","CA47","CA48","CA49","CA50","CA51","CA52","CA53","CO01","CO02","CO03","CO04","CO05","CO06","CO07","CT01","CT02","CT03","CT04","CT05","DE01","FL01","FL02","FL03","FL04","FL05","FL06","FL07","FL08","FL09","FL10","FL11","FL12","FL13","FL14","FL15","FL16","FL17","FL18","FL19","FL20","FL21","FL22","FL23","FL24","FL25","FL26","FL27","GA01","GA02","GA03","GA04","GA05","GA06","GA07","GA08","GA09","GA10","GA11","GA12","GA13","GA14","HI01","HI02","ID01","ID02","IL01","IL02","IL03","IL04","IL05","IL06","IL07","IL08","IL09","IL10","IL11","IL12","IL13","IL14","IL15","IL16","IL17","IL18","IN01","IN02","IN03","IN04","IN05","IN06","IN07","IN08","IN09","IA01","IA02","IA03","IA04","KS01","KS02","KS03","KS04","KY01","KY02","KY03","KY04","KY05","KY06","LA01","LA02","LA03","LA04","LA05","LA06","ME01","ME02","MD01","MD02","MD03","MD04","MD05","MD06","MD07","MD08","MA01","MA02","MA03","MA03","MA05","MA06","MA07","MA08","MA09","MI01","MI02","MI03","MI04","MI05","MI06","MI07","MI08","MI09","MI10","MI11","MI12","MI13","MI14","MN01","MN02","MN03","MN04","MN05","MN06","MN07","MN08","MS01","MS02","MS03","MS04","MO01","MO02","MO03","MO04","MO04","MO06","MO07","MO08","MT01","NE01","NE02","NE03","NV01","NV02","NV03","NV04","NH01","NH02","NJ01","NJ02","NJ03","NJ04","NJ05","NJ06","NJ07","NJ08","NJ09","NJ10","NJ11","NJ12","NM01","NM02","NM03","NY01","NY02","NY03","NY04","NY05","NY06","NY07","NY08","NY09","NY10","NY11","NY12","NY13","NY14","NY15","NY16","NY17","NY18","NY19","NY20","NY21","NY22","NY23","NY24","NY25","NY26","NY27","NC01","NC02","NC03","NC04","NC05","NC06","NC07","NC08","NC09","NC10","NC11","NC12","NC13","ND01","OH01","OH02","OH03","OH04","OH05","OH06","OH07","OH08","OH09","OH10","OH11","OH12","OH13","OH14","OH15","OH16","OK01","OK02","OK03","OK04","OK05","OR01","OR02","OR03","OR04","OR05","PA01","PA02","PA03","PA04","PA05","PA06","PA07","PA08","PA09","PA10","PA11","PA12","PA13","PA14","PA15","PA16","PA17","PA18","RI01","RI02","SC01","SC02","SC03","SC04","SC05","SC06","SC07","SD01","TN01","TN02","TN03","TN04","TN05","TN06","TN07","TN08","TN09","TX01","TX02","TX03","TX04","TX05","TX06","TX07","TX08","TX09","TX10","TX11","TX12","TX13","TX14","TX15","TX16","TX17","TX18","TX19","TX20","TX21","TX22","TX23","TX24","TX25","TX26","TX27","TX28","TX29","TX30","TX31","TX32","TX33","TX34","TX35","TX36","UT01","UT02","UT03","UT04","VT01","VA01","VA02","VA03","VA04","VA05","VA06","VA07","VA08","VA09","VA10","VA11","WA01","WA02","WA03","WA04","WA05","WA06","WA07","WA08","WA09","WA10","WV01","WV02","WV03","WI01" ,"WI02","WI03","WI04","WI05","WI06","WI07","WI08","WY01"]
            if a not in listuser:
            
            
               self.add_error("district", forms.ValidationError("please enter a valid district"))

        confirm_password = cleaned_data.get("confirmation")

        if password != confirm_password:
             self.add_error("confirmation", forms.ValidationError("password and confirm_password does not match") 
            # raise forms.ValidationError(
            #     "password and confirm_password does not match"
            )  
       
       
       
       
   

        
