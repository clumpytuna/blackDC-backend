from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from .api_well import get_one


@api_view(['GET'])
def get_one_well(request):
    """
    Upload view for the user.
    """
    return JsonResponse(get_one(request), safe=False)
