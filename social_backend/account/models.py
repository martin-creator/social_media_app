import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone



class CustomUserManager(UserManager):
    '''
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    This class inherits from the UserManager class which is a built-in class in Django that handles the creation and management of user accounts in the database.

    '''
    def _create_user(self, name, email, password, **extra_fields):
        if not email:
            raise ValueError('Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db) # using=self._db is used to specify the database to use when saving the user.

        return user

    def create_user(self,  name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(name, email, password, **extra_fields)


    def create_superuser(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(name, email, password, **extra_fields)

# Create your models here.
