from django.contrib.auth.models import AbstractUser
from django.db import models
# accounts/models.py


class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)

    def __str__(self):
        return self.username

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)

# Create your models here.
