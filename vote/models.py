from turtle import update
from venv import create
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager
import uuid



# Create your models here.
class user(AbstractBaseUser,PermissionsMixin):
    district=models.CharField(max_length=200)
    voterid=models.IntegerField(max_length=200,null=True)
    name=models.CharField(max_length=200)
    email=models.EmailField(_('email'),unique=True)
    password=models.CharField(max_length=200)
    confirmation=models.CharField(max_length=200)
    upload=models.ImageField(upload_to='images/',null=True,blank=True)
    is_staff 	= models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.')
    is_active 	= models.BooleanField(default=True,
		help_text='Designates whether this user should be treated as active.\
		Unselect this instead of deleting accounts.')
    USERNAME_FIELD 	='email'
    objects = CustomUserManager()

    def __str__(self):
        return self.email

class pod(models.Model):
  pod_key =  models.CharField(unique=True, editable=False,max_length=6)
  pod_owner_id=models.ForeignKey(user,on_delete=models.CASCADE,null=True)