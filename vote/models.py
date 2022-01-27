from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager
import uuid
from django.core.validators import validate_comma_separated_integer_list



# Create your models here.
class user(AbstractBaseUser,PermissionsMixin):
    district=models.CharField(max_length=200)
    voterid=models.IntegerField(max_length=200,null=True)
    name=models.CharField(max_length=200)
    email=models.EmailField(_('email'),unique=True,blank=True)
    password=models.CharField(max_length=200)
    confirmation=models.CharField(max_length=200)
    upload=models.ImageField(upload_to='images/',null=True,blank=True)
    is_staff 	= models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.')
    is_active 	= models.BooleanField(default=True,
		help_text='Designates whether this user should be treated as active.\
		Unselect this instead of deleting accounts.')
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at =  models.DateTimeField(auto_now=True)


    USERNAME_FIELD 	='email'
    objects = CustomUserManager()

    def __str__(self):
        return self.email

class pod(models.Model):
  pod_key =  models.CharField(unique=True, editable=False,max_length=6)
  pod_owner_id=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
  created_at = models.DateTimeField(auto_now_add=True,null=True)
  updated_at =  models.DateTimeField(auto_now=True)


class pod_member(models.Model):
  pod_id=models.ForeignKey(pod,on_delete=models.CASCADE,null=True)
  member_id=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
  count=models.IntegerField(default=0)
  verify_id=models.CharField(validators=[validate_comma_separated_integer_list],null=True,blank=True,max_length=200,default="")
  created_at = models.DateTimeField(auto_now_add=True,null=True)  
  updated_at =  models.DateTimeField(auto_now=True)


