from django.urls import path
from vote.Views import Loginview
from vote.Views import Signupview
from vote.Views import Keyview
from vote.Views import Podview
from vote.Views import memberview
from vote.Views import fdkeyview
from vote.Views import fpodview

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
    path('join',Podview.validate,name="join"),
    path("show",Podview.podshow,name='show'), 

    
#fpod urls
    path('fjoin',fpodview.fvalidate,name="fjoin"),
    path("fshow",fpodview.fpodshow,name='fshow'), 

#key urls
    path("pod",Keyview.key_generator,name="key"),
    path('pod/<int:id>', Keyview.show, name="key2"), 
    # path("show<int:id>",Keyview.keyshow,name='show2'),

#fdelkey urls 
    path("fpod",fdkeyview.fkey_generator,name="fkey"),
    path('fpod/<int:id>', fdkeyview.fshow, name="fkey2"), 


#member urls
path('member',memberview.memberIndex,name="member_index"),

#vote_second_group

# path('Hellouser',helloUser.index,name="hello_user"),


    

]

        