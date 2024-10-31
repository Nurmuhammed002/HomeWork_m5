from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from users.serializers import UserCreateSerializer, ConfirmUserSerializer

@api_view(['POST'])
def registration_api_view(request):
    serializer = UserCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.save()

    return Response(status=status.HTTP_201_CREATED,
                    data={'user_id': user.id, 'confirmation_code': user.confirmation_code})

@api_view(['POST'])
def confirm_user_api_view(request):
    serializer = ConfirmUserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    serializer.save()

    return Response(status=status.HTTP_200_OK, data={'message': 'User confirmed successfully.'})
