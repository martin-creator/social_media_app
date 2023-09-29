import email
from enum import auto
from http.client import ACCEPTED
import uuid
from account.models import User
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

class User(AbstractBaseUser, PermissionsMixin):
    '''
    Custom user model that supports using email instead of username
    It inherits from the AbstractBaseUser class which is a built-in class in Django that provides the core implementation of a user model.
    It also inherits from the PermissionsMixin class which is a built-in class in Django that provides the implementation of the permissions model.

    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True) # unique=True is used to specify that the email field must be unique throughout the database.
    name = models.CharField(max_length=255, default='', blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    friends = models.ManyToManyField('self', blank=True)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager() # This is used to specify the custom user manager to use for managing the user accounts.

    USERNAME_FIELD = 'email' # This is used to specify the field to use for logging in. In this case, we are using the email field.
    EMAIL_FIELD = 'email' # This is used to specify the email field. In this case, we are using the email field.
    REQUIRED_FIELDs = []


    class FriendshipRequest(models.Model):
        '''
        Model for friendship requests

        '''

    SENT = 'sent'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'

    STATUS_CHOICES = (
        (SENT, 'Sent'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_for = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_friendrequests')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_friendrequests')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=SENT)

    
