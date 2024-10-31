from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
import random

class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField()
    email = serializers.EmailField()
    confirmation_code = serializers.CharField(read_only=True)

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise ValidationError('User already exists!')
        return username

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            is_active=False
        )
        user.set_password(validated_data['password'])
        user.confirmation_code = self.generate_confirmation_code()
        user.save()
        return user

    def generate_confirmation_code(self):
        return f"{random.randint(100000, 999999)}"

class ConfirmUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField(max_length=6)

    def validate(self, attrs):
        try:
            user = User.objects.get(username=attrs['username'])
            if user.confirmation_code != attrs['confirmation_code']:
                raise ValidationError("Invalid confirmation code.")
        except User.DoesNotExist:
            raise ValidationError("User does not exist.")

        return attrs

    def save(self):
        user = User.objects.get(username=self.validated_data['username'])
        user.is_active = True
        user.confirmation_code = None
        user.save()
