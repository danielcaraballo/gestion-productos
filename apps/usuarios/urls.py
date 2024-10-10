from django.urls import path
from .views import SomeProtectedView, UpdateProfileView, ChangePasswordView, UserProfileView, ChangeEmailView

urlpatterns = [
    path('protected/', SomeProtectedView.as_view(),
         name='protected'),  # Vista protegida
    path('profile-data/', UserProfileView.as_view(),
         name='profile-data'),  # Obtener datos de perfil
    path('update-profile/', UpdateProfileView.as_view(),
         name='update-profile'),  # Actualizar perfil
    path('change-password/', ChangePasswordView.as_view(),
         name='change-password'),  # Cambiar contraseña
    path('change-email/', ChangeEmailView.as_view(),
         name='change-email'),  # Cambiar correo electrónico
]
