from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'content', 'author', 'created_at', 'updated_at']

    @staticmethod
    def validate_title(value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty")
        return value

    @staticmethod
    def validate_description(value):
        if not value.strip():
            raise serializers.ValidationError("Description cannot be empty")
        return value

    @staticmethod
    def validate_content(value):
        if not value.strip():
            raise serializers.ValidationError("Content cannot be empty")
        return value
