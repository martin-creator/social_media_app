from django.shortcuts import render
from django.http import JsonResponse
from .serializers import PostSerializer
from .models import Post
from rest_framework.decorators import api_view, permission_classes, authentication_classes

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return JsonResponse({'data': serializer.data})
