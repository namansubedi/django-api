from django.shortcuts import render
from rest_framework import serializers

from api.models import Blogs
from .serializers import BlogsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes

# Create your views here.

@api_view(['GET'])
def listOf(request):
    urlList = [
        'viewSomeBlog/',
        'inputBlog/',
        'outputBlog/'
    ]
    return Response(urlList)

#returns every blog in the database
@api_view(['GET'])
def viewSomeBlog(request):
    blogs = Blogs.objects.all()
    serializer = BlogsSerializer(blogs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def inputBlog(request):
    serializer = BlogsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#returns one blog from the database according to the pk passed
@api_view(['GET'])
def outputBlog(request, pk):
    try:
        blogs = Blogs.objects.get(id = pk)
    except:
        blogs = "No Such Tuple Found"
    serializer = BlogsSerializer(blogs, many=True)
    return Response(serializer.data)