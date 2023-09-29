import re
from venv import create
from django.http import JsonResponse

from rest_framework.decorators import api_view, permission_classes, authentication_classes

from .forms import SignupForm
from .models import User, FriendshipRequest
from .serializers import UserSerializer, FriendshipRequestSerializer


@api_view(['GET'])
def me(request):
    '''
    A view for getting the current user's information.

    '''
    user = request.user

    return JsonResponse({
        'id': user.id,
        'email': user.email,
        'name': user.name,
    })


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    '''
    A view for creating new users.

    '''
    data = request.data
    message = 'success'

    form = SignupForm({
        'email': data['email'],
        'name': data['name'],
        'password1': data['password1'],
        'password2': data['password2'],
    })

    if form.is_valid():
        user = form.save()
        user.is_active = True
        user.save()

        # send verification email later
    else:
        message = form.errors.as_json()

        print(message

              )

    return JsonResponse({'message': message}, status=201, safe=False)


@api_view(['POST'])
def send_friendship_request(request, pk):
    '''
    A view for sending a friendship request to another user.

    '''
    user = User.objects.get(pk=pk)

    check1 = FriendshipRequest.objects.filter(created_for=request.user).filter(created_by=user)
    check2 = FriendshipRequest.objects.filter(created_for=user).filter(created_by=request.user)

    if not check1 or not check2:
        friendrequest = FriendshipRequest.objects.create(created_for=user, created_by=request.user)

        #notification = create_notification(request, 'new_friendrequest', friendrequest_id=friendrequest.id)

        return JsonResponse({'message': 'friendship request created'})
    else:
        return JsonResponse({'message': 'request already sent'})



@api_view(['GET'])
def friends(request, pk):
    '''
    A view for getting a user's friends.

    '''
    user = User.objects.get(pk=pk)
    requests = []

    if user == request.user:
        requests = FriendshipRequest.objects.filter(created_for=request.user, status=FriendshipRequest.SENT)
        requests = FriendshipRequestSerializer(requests, many=True)
        requests = requests.data

    friends = user.friends.all()

    return JsonResponse({
        'user': UserSerializer(user).data,
        'friends': UserSerializer(friends, many=True).data,
        'requests': requests
    }, safe=False)


@api_view (['POST'])
def handle_request(request, pk, status):
    '''
    A view for handling friendship requests.

    '''
    user = User.objects.get(pk=pk)


    frs = FriendshipRequest.objects.filter(created_for=request.user).get(created_by=user)
    friendship_request = FriendshipRequest.objects.filter(
        created_for=request.user).get(created_by=user)
    friendship_request.status = status
    friendship_request.save()

    user.friends.add(request.user)
    user.friends_count = user.friends.count + 1
    user.save()

    request_user  = request.user
    request_user.friends_count = request_user.friends.count + 1
    request_user.save()

    return JsonResponse({'message': 'Friendship request updated successfully.'}, status=201, safe=False)
