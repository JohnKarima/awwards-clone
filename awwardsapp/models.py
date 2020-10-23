from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
from django.db.models.signals import pre_delete
import cloudinary
import datetime as dt


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    bio = models.TextField(null=True)
    profile_photo = CloudinaryField('profile_photo', null=True)

    def __str__(self):
        return f'{self.user.username} Profile'



class Project(models.Model):
    title = models.CharField(max_length = 60)
    project_image = CloudinaryField('project_image', null=True)
    description = models.TextField()
    link = models.CharField(max_length = 200, null=True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user_ref = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='projects', null=True)

    class Meta:
        '''
        Class method to display images by date published
        '''
        ordering = ['pub_date']