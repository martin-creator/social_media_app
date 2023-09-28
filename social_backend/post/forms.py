from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    '''
    A form for creating new posts.
    
    '''

    class Meta:
        model = Post
        fields = ['body',]