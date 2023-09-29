from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from account.models import User
from post.models import Post
from account.serializers import UserSerializer
from post.serializers import PostSerializer

@api_view(['POST'])
def search(request):
    data = request.data
    query = data['query']

    users = User.objects.filter(name__icontains=query)  # __icontains is case insensitive
    users_serializer = UserSerializer(users, many=True)

    # First, filter User objects whose names match the query
    matching_users = User.objects.filter(name__icontains=query)

    # Then, filter Post objects based on the users found in the previous step
    posts = Post.objects.filter(body__icontains=query, created_by__in=matching_users) &  Post.objects.all()[:5]

    posts_serializer = PostSerializer(posts, many=True)

    return JsonResponse({'users': users_serializer.data, 'posts': posts_serializer.data}, safe=False)