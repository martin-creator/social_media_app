from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes

@api_view(['POST'])
def search(request):
    data = request.data
    query = data['query']

    print(query)

    return JsonResponse({'data': 'it works'})