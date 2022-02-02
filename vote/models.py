from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager
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
    address=models.CharField(max_length=100,null=True)
    executed_on=models.DateField(null=True)
    registered=models.IntegerField(default=0)
    eligible=models.IntegerField(default=0)
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

class pod_groups(models.Model):
  group_key =  models.CharField(unique=True, editable=False,max_length=6)
  group_owner=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
  created_at = models.DateTimeField(auto_now_add=True,null=True)
  updated_at =  models.DateTimeField(auto_now=True)


class pod_groups_members(models.Model):
  group=models.ForeignKey(pod_groups,on_delete=models.CASCADE,null=True)
  member=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
  vote_count=models.IntegerField(default=0)
  elect_count=models.IntegerField(default=0)
  member_status = models.IntegerField(null=True) 
  member_comment = models.TextField(max_length=500,null=True)
  vote_given=models.IntegerField(default=0)
  elect_vote_given=models.IntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True,null=True)  
  updated_at =  models.DateTimeField(auto_now=True)


# class elect_count(models.Model):
#   Elect_count=models.IntegerField(default=1)
#   Elect_user=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
#   Elect_member=models.ForeignKey(pod_member,on_delete=models.CASCADE,null=True)