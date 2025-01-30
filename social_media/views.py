from django.shortcuts import render

# importing neccessary modules from Django and Framework:
from rest_framework import viewsets
from .models import User, Post, Comment 
from .serializers import UserSerializer, PostSerializer, CommentSerializer

# viewset handles the user models
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer