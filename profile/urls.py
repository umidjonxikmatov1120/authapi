from django.urls import path
from .views import RegistrationView, ProfileView

urlpatterns = [
    path('profile/register/', RegistrationView.as_view(), name='register'),
    path('profile/profile/', ProfileView.as_view(), name='profile'),
]
