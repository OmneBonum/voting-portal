
from argparse import Namespace
from unicodedata import name
from django.urls import path
from vote.Views import Loginview
from vote.Views import Signupview
from vote.Views import Keyview
from vote.Views import Podview
from . import views
app_name = "vote"


urlpatterns = [
    path('', Loginview.index, name='html'),
    path("login",Loginview.user_login,name='login'),
    path('logout',Loginview.userLogout,name='logout'),
    path("help",views.help,name='help'),


# signup urls  
    path("",Signupview.index),
    path("create",Signupview.create,name='signupcreate'),
    path("update/<int:id>",Signupview.update,name='signupupdate'),

# POD urls  

    path("show",Podview.show,name='show'),
    path('join',Podview.validate,name="join"),
    #path('show2/<int:id>', Podview.mypod, name="shows"), 
    
#key urls
    path("pod",Keyview.key_generator,name="key"),
    path('pod/<int:id>', Keyview.show, name="key2"), 
    path("view/<int:id>",Keyview.show2,name='view'), 

    

]

        