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
    prof_ref = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='projects', null=True)

    class Meta:
    
        ordering = ['pub_date']
    
    def __str__(self):
        return self.title



RATE_CHOICES = [
    (1,'1-Dung'),
    (2,'2-Troll'),
    (3,'3-Awful'),
    (4,'4-Poor'),
    (5,'5-Average'),
    (6,'6-Barely Above Average'),
    (7,'7-Good'),
    (8,'Excellent'),
    (9,'Exceeds Expectations'),
    (10,'10-Outstanding'),
]

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    review = models.TextField(null=True)
    rate_design = models.PositiveSmallIntegerField(choices = RATE_CHOICES)
    rate_usability = models.PositiveSmallIntegerField(choices = RATE_CHOICES)
    rate_content = models.PositiveSmallIntegerField(choices = RATE_CHOICES)

    def __str__(self):
        return self.user.username