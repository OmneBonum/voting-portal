from django.urls import path
from vote.Views import Loginview
from vote.Views import Signupview
from vote.Views import Keyview
from vote.Views import Podview
from vote.Views import memberview
from vote.Views import fdkeyview
from vote.Views import fpodview
from vote.Views import sdkeyview
from vote.Views import tdkeyview
from vote.Views import spodview
from vote.Views import tpodview
from vote.Views import fifthdelpodview
from vote.Views import fourthkeyview
from vote.Views import fourthpodview
from vote.Views import fifthdelkeyview
from vote.Views import sixthdelkeyview
from vote.Views import sixthdelpodview

app_name = "vote"


urlpatterns = [
    path('', Loginview.index, name='html'),
    path("login",Loginview.user_login,name='login'),
    path('logout',Loginview.userLogout,name='logout'),
    path("help",Loginview.help,name='help'),


# signup urls  
    path("create",Signupview.create,name='signupcreate'),
    path("update/<int:id>",Signupview.update,name='signupupdate'),

# POD urls  
    path("show",Podview.podshow,name='show'), 
    path('join',Podview.validate,name="join"),
    
#fpod urls
    path('fjoin',fpodview.fvalidate,name="fjoin"),
    path("fshow",fpodview.fpodshow,name='fshow'), 

#spod urls
    path('sjoin',spodview.svalidate,name="sjoin"),
    path("sshow",spodview.spodshow,name='sshow'), 

#tpod urls
    path('tjoin',tpodview.tvalidate,name="tjoin"),
    path("tshow",tpodview.tpodshow,name='tshow'), 

#fourth pod  urls
    path('fojoin',fourthpodview.fourthvalidate,name="fojoin"),
    path("foshow",fourthpodview.fourthpodshow,name='foshow'), 
     

#fifthpod urls
    path('fijoin',fifthdelpodview.fifthvalidate,name="fijoin"),
    path("fishow",fifthdelpodview.fifthpodshow,name='fishow'), 


#sixthpod urls
    path("fishow",sixthdelpodview.sixthpodshow,name='fishow'), 
    path('fijoin',sixthdelpodview.sixthvalidate,name="fijoin"),
    

#key urls
    path("pod",Keyview.key_generator,name="key"),
    path('pod/<int:id>', Keyview.show, name="key2"), 
    # path("show<int:id>",Keyview.keyshow,name='show2'),

#fdelkey urls 
    path("fpod",fdkeyview.fkey_generator,name="fkey"),
    path('fpod/<int:id>', fdkeyview.fshow, name="fkey2"), 

#sdelkey urls 
    path("spod",sdkeyview.skey_generator,name="skey"),
    path('spod/<int:id>', sdkeyview.sshow, name="skey2"), 

#tdelkey urls
    path("tpod",tdkeyview.tkey_generator,name="tkey"),
    path('tpod/<int:id>', tdkeyview.tshow, name="tkey2"), 

  
#fourthdelkey urls
    path("fopod",fourthkeyview.fourthkey_generator,name="fokey"),
    path('fopod/<int:id>', fourthkeyview.fourthshow, name="fokey2"), 

#fifthdelkey urls
    path("fipod",fifthdelkeyview.fifthkey_generator,name="fikey"),
    path('fipod/<int:id>', fifthdelkeyview.fifthshow, name="fikey2"),


#sixthdelkey urls
    path("sipod",sixthdelkeyview.sixthkey_generator,name="sikey"),
    path('sipod/<int:id>', sixthdelkeyview.sixthshow, name="sikey2"),     







#member urls
path('member',memberview.memberIndex,name="member_index"),










#vote_second_group

# path('Hellouser',helloUser.index,name="hello_user"),


    

]

        