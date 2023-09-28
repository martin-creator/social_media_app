from asyncore import read
from .models import Post, PostAttachment
from rest_framework import serializers
from account.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'body', 'created_at_formatted', 'created_by', 'attachments' ]

