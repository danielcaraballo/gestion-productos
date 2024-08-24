from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from .serializers import UserSerializer


# Create your views here.


class SomeProtectedView(APIView):       # Vista protegida que requiere autenticación
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "This is a protected view"})


class RegisterView(APIView):    # Vista de registro de usuarios
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(
                username=serializer.validated_data['username'],
                email=serializer.validated_data['email'],
                password=request.data['password']
            )
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateProfileView(generics.UpdateAPIView):    # Vista para actualizar usuarios
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class ChangePasswordView(APIView):      # Vista para cambiar la contrasena
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        form = PasswordChangeForm(user=user, data=request.data)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return Response({"message": "Password changed successfully"}, status=status.HTTP_200_OK)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
