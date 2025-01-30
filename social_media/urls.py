# importing modules:
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PostViewSet, CommentViewSet

# creating router instance to manage API
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

# Define URL Patterns for API
urlpatterns = [path("", include(router.urls)),]