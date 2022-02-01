from django.urls import path
from vote.Views import Loginview
from vote.Views import Signupview
from vote.Views import Keyview
from vote.Views import Podview
from vote.Views import memberview
from . import viewssss
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

#key urls
    path("pod",Keyview.key_generator,name="key"),
    path('pod/<int:id>', Keyview.show, name="key2"), 
    # path("show<int:id>",Keyview.keyshow,name='show2'),

#member urls
path('member',memberview.memberIndex,name="member_index"),

#

    

]

        