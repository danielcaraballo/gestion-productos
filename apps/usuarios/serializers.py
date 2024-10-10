from django.contrib.auth.models import User
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def update(self, instance, validated_data):
        # Actualiza los campos del usuario
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def validate_email(self, value):
        # Valida que el correo electrónico no esté en uso por otro usuario
        if User.objects.exclude(pk=self.instance.pk).filter(email=value).exists():
            raise serializers.ValidationError(
                "Este correo electrónico ya está en uso.")
        return value


class ChangeEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']

    def validate_email(self, value):
        # Valida que el correo electrónico no esté en uso por otro usuario
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError(
                "Este correo electrónico ya está en uso.")
        return value


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate(self, data):
        # Valida que las nuevas contraseñas coincidan y que cumplan con los requisitos
        new_password = data.get('new_password')
        confirm_password = data.get('confirm_password')

        if new_password != confirm_password:
            raise serializers.ValidationError(
                "Las contraseñas nuevas no coinciden.")

        if len(new_password) < 8:  # Ejemplo: mínimo 8 caracteres
            raise serializers.ValidationError(
                "La nueva contraseña debe tener al menos 8 caracteres.")

        return data

    def validate_old_password(self, value):
        # Valida que la contraseña antigua sea correcta
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                "La contraseña actual es incorrecta.")
        return value
