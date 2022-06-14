from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from tinymce.models import HTMLField


class Profile(models.Model):
    profile_pic = models.ImageField( upload_to='profile/', blank ='true',default='default.png')
    bio = models.TextField()
    user =models.OneToOneField(User, on_delete = models.CASCADE)
    date_craeted= models.DateField(auto_now_add=True )


    