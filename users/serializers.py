from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
import random

class UserCreateSerializer(serializers.ModelSerializer):
    confirmation_code = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'confirmation_code']

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
        user = User.objects.filter(username=attrs['username']).first()
        if user is None:
            raise ValidationError("User does not exist.")
        if user.confirmation_code != attrs['confirmation_code']:
            raise ValidationError("Invalid confirmation code.")
        return attrs
