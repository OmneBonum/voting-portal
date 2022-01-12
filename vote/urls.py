from django.urls import path
from vote.Views import Loginview
from vote.Views import Signupview
from . import views


urlpatterns = [
    path('', Loginview.index, name='html'),
    #path("signup",Signupview.index,name='signup'),
    path("signup",Signupview.create,name='signup'),
    path("login",Loginview.login,name='login'),
    path("help",views.help,name='help'),
]