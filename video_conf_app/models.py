from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser): 
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True) 
    
    def __str__(self):
        return f"{self.username}"