from django.urls import path
from .views import RegisterView, SomeProtectedView, UpdateProfileView, ChangePasswordView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('protected/', SomeProtectedView.as_view(), name='protected'),
    path('profile/', UpdateProfileView.as_view(), name='update_profile'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
]