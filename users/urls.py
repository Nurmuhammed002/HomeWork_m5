from django.urls import path
from .views import registration_api_view, confirm_user_api_view

urlpatterns = [
    path('api/v1/users/register/', registration_api_view, name='registration'),
    path('api/v1/users/confirm/', confirm_user_api_view, name='confirm_user'),
]
