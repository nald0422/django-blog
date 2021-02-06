from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from rest_framework import generics

from django_filters.rest_framework import DjangoFilterBackend

from .models import Blog
from .serializers import BlogSerializer

# Create your views here.


class BlogView(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = BlogSerializer

    filter_fields =  ["author", "title"]

    
# @api_view(['GET'])
# def blogApiOverview(request):
#     api_urls = {
#         'List': '/blog-list/',
#         'Detail View':'/blog-detail/<str:pk>/',
#         'Create':'/blog-create/',
#         'Update':'/blog-update/<str:pk>/',
#         'Delete':'/blog-delete/<str:pk>/',
#     }
#     return Response(api_urls)

# @api_view(['GET'])
# def blogList(request):
#     blogs = Blog.objects.all()

#     serializer = BlogSerializer(blogs, many=True, context = {'request':request})
#     return Response(serializer.data)

# @api_view(['GET'])
# def blogDetail(request, pk):
#     blog = Blog.objects.get(id=pk)
#     serializer = BlogSerializer(blog, many=False)
#     return Response(serializer.data)

# @api_view(['POST'])
# def blogCreate(request):
#     serializer = BlogSerializer(data=request.data, context = {'request': request})
    
#     if serializer.is_valid():
#         serializer.save()
#     else:
#         print('failed')

#     return Response(serializer.data)

# @api_view(['POST'])
# def blogUpdate(request, pk):
#     blog = Blog.objects.get(id=pk)
#     serializer = BlogSerializer(instance=blog, data=request.data, context={'request':request})
    
#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)

# @api_view(['DELETE'])
# def blogDelete(request, pk):
#     blog = Blog.objects.get(id=pk)
#     blog.delete()

#     return Response('Item successfully deleted')
