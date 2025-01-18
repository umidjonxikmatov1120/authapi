from django.urls import path
from .views import RegistrationView, ProfileView

urlpatterns = [
    path('user/register/', RegistrationView.as_view(), name='register'),
    path('user/user/', ProfileView.as_view(), name='user'),
]
