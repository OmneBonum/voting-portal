from django.urls import path
from vote.Views import Loginview
from vote.Views import Signupview
from vote.Views import Keyview
from . import views
app_name = "vote"


urlpatterns = [
    path('', Loginview.index, name='html'),
    path("login",Loginview.login,name='login'),
    path("help",views.help,name='help'),


# signup urls  
    path("pod",Signupview.index,name='pod'),
    path("signup/create",Signupview.create,name='signupcreate'),
    path("signup/update/<int:id>",Signupview.update,name='signupupdate'),


# # POD urls  
#     # path("signup/create",Signupview.index,name='signup'),
#     path("pod/p",Signupview.create,name='podview'),
    
#key urls
    path("key",Keyview.key_generator,name="key")

]

        