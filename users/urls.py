from django.urls import path
from users import views

urlpatterns = [
    path('api/v1/users/register/', views.RegistrationAPIView.as_view(), name='registration'),
    path('api/v1/users/confirm/', views.ConfirmUserAPIView.as_view(), name='confirm_user'),
]
