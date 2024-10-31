from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from users.serializers import UserCreateSerializer, ConfirmUserSerializer

class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        return Response(status=status.HTTP_201_CREATED,
                        data={'user_id': user.id, 'confirmation_code': user.confirmation_code})

class ConfirmUserAPIView(APIView):
    def post(self, request):
        serializer = ConfirmUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.get(username=serializer.validated_data['username'])
        user.is_active = True
        user.confirmation_code = None
        user.save()

        return Response(status=status.HTTP_200_OK, data={'message': 'User confirmed successfully.'})
