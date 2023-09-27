from django.contrib.auth.forms import UserCreationForm

from .models import User


class SignupForm(UserCreationForm):
    '''
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    Inherits from the UserCreationForm class which is a built-in class in Django that provides the implementation of a form for creating new users.
    
    '''
    class Meta:
        model = User
        fields = ('email', 'name', 'password1', 'password2')