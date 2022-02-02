from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# third party imports
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from .serializers import PostSerializer
from .models import Post



# Create your views here.

# def test_view(request):
#   data = {
#     'name' : 'Saurav',
#     'desc' : "Hi, I am saurav chaudhary"
#   }
#   return JsonResponse(data)   # safe=False, for passing list

# class TestView(APIView):
#   def get(self, request, *args, **kwargs):
#     data = {
#       'name': 'saurav',
#       'desc': 'i am from Nepal'
#     }
#     return Response(data)

# class TestView(APIView):
#   def get(self, request, *args, **kwargs):
#     # data = {
#     #   'name': 'saurav',
#     #   'desc': 'i am from Nepal'
#     # }
#     qs = Post.objects.all()
#     post = qs.first()
#     # serializer = PostSerializer(post)
#     serializer = PostSerializer(qs, many=True)
#     return Response(serializer.data)

#   def post(self, request, *args, **kwargs):
#     serializer = PostSerializer(data=request.data);
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data)
#     return Response(serializer.errors)


# class PostView(
#   mixins.ListModelMixin,
#   mixins.CreateModelMixin,
#   generics.GenericAPIView):
  
#   serializer_class = PostSerializer
#   queryset = Post.objects.all()

#   def get(self, request, *args, **kwargs):
#     return self.list(request, args, kwargs)
  
#   def post(self, request, *args, **kwargs):
#     return self.create(request, args, kwargs )

# class PostCreateView(mixins.ListModelMixin, generics.CreateAPIView):
#   serializer_class = PostSerializer
#   queryset = Post.objects.all()

#   def get(self, request, *args, **kwargs):
#     return self.list(request, args, kwargs)
  

class PostListCreateView(generics.ListCreateAPIView):
  serializer_class = PostSerializer
  queryset = Post.objects.all()
  