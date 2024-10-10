from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from .serializers import UserProfileSerializer, ChangeEmailSerializer


# Vista protegida que requiere autenticación
class SomeProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "This is a protected view"})


# Vista para obtener el perfil del usuario autenticado
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)


# Vista para actualizar el perfil del usuario
class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


# Vista para cambiar la contraseña
class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        form = PasswordChangeForm(user=user, data=request.data)
        if form.is_valid():
            user = form.save()
            # Actualiza la sesión para mantener el usuario autenticado
            update_session_auth_hash(request, user)
            return Response({"message": "Password changed successfully"}, status=status.HTTP_200_OK)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


# Vista para cambiar el correo electrónico
class ChangeEmailView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        serializer = ChangeEmailSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos actualizados!'}, status=status.HTTP_200_OK)

        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
