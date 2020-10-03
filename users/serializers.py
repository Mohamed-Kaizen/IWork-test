"""Collection serializers."""
from typing import Any, Dict

from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth.password_validation import validate_password
from rest_framework import exceptions, serializers

from .models import CustomUser
from .validators import (
    validate_confusables,
    validate_confusables_email,
    validate_reserved_name,
)


class UserDetailsSerializer(serializers.Serializer):
    """User detail serializer."""

    email = serializers.EmailField(read_only=True)

    username = serializers.CharField(read_only=True)

    picture = serializers.ImageField(read_only=True)

    is_active = serializers.BooleanField(read_only=True)


class JWTSerializer(serializers.Serializer):
    """JWT serializer."""

    access_token = serializers.CharField(read_only=True)

    refresh_token = serializers.CharField(read_only=True)

    user = UserDetailsSerializer(read_only=True)


class CustomRegisterSerializer(RegisterSerializer):
    """Custom Register serializer."""

    full_name = serializers.CharField(max_length=300)

    def get_cleaned_data(self: "CustomRegisterSerializer") -> Dict[str, Any]:
        """Cleaning for input data."""
        data_dict = super().get_cleaned_data()
        data_dict["full_name"] = self.validated_data.get("full_name", "")

        return data_dict


class UserSignUpSerializer(serializers.ModelSerializer):
    """User signup serializer."""

    class Meta:
        """Meta data."""

        model = CustomUser
        fields = (
            "username",
            "password",
            "email",
            "full_name",
        )
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}}
        }

    def validate_password(self: "UserSignUpSerializer", value: str) -> str:
        """Password validation."""
        validate_password(value, self.instance)
        return value

    def create(self: "UserSignUpSerializer", validated_data: Dict) -> CustomUser:
        """Create method for UserSignUpSerializer."""
        password = validated_data.pop("password")

        username = validated_data.get("username")

        email = validated_data.get("email")

        local, domain = email.split("@")

        validate_reserved_name(
            value=username, exception_class=exceptions.ValidationError
        )

        validate_reserved_name(value=local, exception_class=exceptions.ValidationError)

        validate_confusables(value=username, exception_class=exceptions.ValidationError)

        validate_confusables_email(
            local_part=local, domain=domain, exception_class=exceptions.ValidationError
        )

        user = CustomUser(**validated_data)

        user.set_password(password)

        user.save()

        return user
