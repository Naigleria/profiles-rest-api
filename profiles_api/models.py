from django.db import models
from django.contrib.auth.models import AbstractBaseuser
from django.contrib.auth.models import PermissionMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile""""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)


class UserProfile(AbstractBaseuser, PermissionMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)

    object = UserProfileManager()

    USERNAME_FIELD= 'email'
    REQUIRED_FIELD= ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email

# Create your models here.
