# accounts/views.py

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()

class UserListView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        users = User.objects.all()  # Fetch all users
        user_data = [{"id": user.id, "username": user.username} for user in users]
        return Response(user_data, status=status.HTTP_200_OK)

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_follow = User.objects.get(id=user_id)
            request.user.following.add(user_to_follow)  # Assuming 'following' is the ManyToMany field
            return Response({"message": f"You are now following {user_to_follow.username}"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_unfollow = User.objects.get(id=user_id)
            request.user.following.remove(user_to_unfollow)  # Assuming 'following' is the ManyToMany field
            return Response({"message": f"You have unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

class FollowingListView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        following = request.user.following.all()
        following_usernames = [user.username for user in following]
        return Response({"following": following_usernames}, status=status.HTTP_200_OK)