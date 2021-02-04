from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from restmigra.models import User
from restmigra.serializers import RestmigraSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def user_list(request):
    if request.method == 'GET':
        tutorials = User.objects.all()
        
        title = request.GET.get('name', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = RestmigraSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = RestmigraSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # elif request.method == 'DELETE':
    #     count = Tutorial.objects.all().delete()
    #     return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    # find tutorial by pk (id)
    try: 
        restmigra = restmigra.objects.get(pk=pk) 
    except User.DoesNotExist: 
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE tutorial
    
        
# @api_view(['GET'])
# def user_list_published(request):
#     # GET all published tutorials
