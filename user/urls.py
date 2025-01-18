from django.urls import path
from .views import RegistrationView, ProfileView

urlpatterns = [
    path('user/register/', RegistrationView.as_view(), name='register'),
    path('user/page/', ProfileView.as_view(), name='page'),
]
