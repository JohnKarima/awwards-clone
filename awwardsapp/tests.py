from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Project
import datetime as dt

class ProfileTestClass(TestCase):
    def setUp(self):
        self.profile = Profile(user='montez', bio='coolbeans', profile_photo='cloudlink.cloud')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))
   
class ProjectTestClass(TestCase):
    def setUp(self):
        self.project = Project(title='tessaract', project_image='cloudlink.cloud', description='3D interpretation of a 4D object', link='tess.com', pub_date='2020', prof_ref='MontezProfile')

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))
