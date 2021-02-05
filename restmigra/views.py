from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from restmigra.models import Product
from restmigra.serializers import RestmigraSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def user_list(request):
    if request.method == 'GET':
        tutorials = Product.objects.all()
        
        title = request.GET.get('name', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=product_name)
        
        tutorials_serializer = RestmigraSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = RestmigraSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'OPTIONS':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = RestmigraSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    tutorial = Product.objects.get(pk=pk)
 
    if request.method == 'GET': 
        tutorial_serializer = RestmigraSerializer(tutorial) 
        return JsonResponse(tutorial_serializer.data) 

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    tutorial = Product.objects.get(pk=pk)
    if request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = RestmigraSerializer(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
