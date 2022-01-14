from django.urls import path
from vote.Views import Loginview
from vote.Views import Signupview
from . import views


urlpatterns = [
    path('', Loginview.index, name='html'),
    path("login",Loginview.login,name='login'),
    path("help",views.help,name='help'),


# signup urls  
    # path("signup/create",Signupview.index,name='signup'),
    path("signup/create",Signupview.create,name='signupcreate'),
    path("signup/update/<int:id>",Signupview.update,name='signupupdate'),

]

        