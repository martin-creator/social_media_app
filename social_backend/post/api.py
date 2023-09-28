from django.http import JsonResponse
from .models import Post
from .forms import PostForm
from .serializers import PostSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes

# Create your views here.


@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    # safe=False is required for objects serialization because we have not serialized a single object but a list of objects.
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def post_create(request):
    form = PostForm(request.data)

    if form.is_valid():
        post = form.save(commit=False)
        post.created_by = request.user
        post.save()

        serializer = PostSerializer(post)

        return JsonResponse(serializer.data, safe=False)

    else:
        return JsonResponse({'error': 'Your form is not valid'}, status=400)
