# importing neccessary modules from Django REST Framework
from rest_framework import serializers

# importing models for User Post and Comment
from .models import User, Post, Comment 

# Serializer for the all Models we're making 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        # fields for our User Model
        fields = ['id', 'username', 'email', 'created_at'] 
        
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields for our Post Model
        fields = ['id', 'user', 'content', 'created_at'] 
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        # fields for our Comment Model
        fields = ['id', 'post', 'user', 'content', 'created_at'] 