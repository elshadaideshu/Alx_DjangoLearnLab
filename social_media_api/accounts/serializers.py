# accounts/serializers.py

from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'bio', 'profile_picture')

    def create(self, validated_data):
        # Create a user instance using the create_user method
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],  # This will hash the password
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None),
        )
        # Create a token for the user
        Token.objects.create(user=user)
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = User.objects.filter(username=data['username']).first()

        if user is None or not user.check_password(data['password']):
            raise serializers.ValidationError("Invalid username or password")

        return data

    def create(self, validated_data):
        user = User.objects.get(username=validated_data['username'])
        token, created = Token.objects.get_or_create(user=user)
        return token.key