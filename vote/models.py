from django.db import models

# Create your models here.
class usersignup(models.Model):
    id=models.AutoField(primary_key=True)
    district=models.CharField(max_length=200)
    voterid=models.IntegerField(max_length=200)
    name=models.CharField(max_length=200)
    email=models.EmailField()
    password=models.CharField(max_length=200)
    confirmation=models.CharField(max_length=200)

