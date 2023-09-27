from django.http import JsonResponse

from rest_framework.decorators import api_view, permission_classes, authentication_classes

from .forms import SignupForm


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
        form.save()

        # send verification email later
    else:
        message = form.errors



    return JsonResponse({'message': message})