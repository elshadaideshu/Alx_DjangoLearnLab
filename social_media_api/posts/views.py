from django.shortcuts import render
# posts/views.py

from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
# posts/views.py

from django_filters.rest_framework import DjangoFilterBackend
# posts/views.py

from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Post
from django.contrib.auth import get_user_model

User = get_user_model()

class PostFeedView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer  # Make sure you have a PostSerializer defined

    def get_queryset(self):
        # Get the current user
        user = self.request.user
        # Get the users that the current user is following
        following_users = user.following.all()
        # Filter posts by authors in the following_users queryset
        return Post.objects.filter(author__in=following_users).order_by('-created_at')  # Assuming 'created_at' is a field in Post

# Additional views for creating, updating, and deleting posts can go here

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# Create your views here.
