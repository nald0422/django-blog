from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets


from django.contrib.auth.models import User
from .serializers import UserSerializer
# Create your views here.

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = UserSerializer

# @api_view(['GET'])
# def apiOverview(request):
#     api_urls = {
#         'List': '/user-list/',
#         'Detail View':'/user-detail/<str:pk>/',
#         'Create':'/user-create/',
#         'Update':'/user-update/<str:pk>/',
#         'Delete':'/user-delete/<str:pk>/',
#     }
#     return Response(api_urls)

# @api_view(['GET'])
# def userList(request):
#     users = User.objects.all()
#     serializer = UserSerializer(users, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def userDetail(request, pk):
#     users = User.objects.get(id=pk)
#     serializer = UserSerializer(users, many=False)
#     return Response(serializer.data)

# @api_view(['POST'])
# def userCreate(request):
#     serializer = UserSerializer(data=request.data)
    
#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)

# @api_view(['POST'])
# def userUpdate(request, pk):
#     user = User.objects.get(id=pk)
#     serializer = UserSerializer(instance=user, data=request.data)
    
#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)

# @api_view(['DELETE'])
# def userDelete(request, pk):
#     user = User.objects.get(id=pk)
#     user.delete()

#     return Response('Item successfully deleted')


