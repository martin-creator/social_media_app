from django.http import JsonResponse

from rest_framework.decorators import api_view, permission_classes, authentication_classes

from .forms import SignupForm
from .models import User

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
        user.is_active = False
        user.save()

        # send verification email later
    else:
        message = form.errors.as_json()

        print(message
        
        )

    return JsonResponse({'message': message}, status=201, safe=False)