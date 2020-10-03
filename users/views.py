"""Collection views."""
from typing import Dict, List

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import CreateAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from .models import CustomUser
from .serializers import UserSignUpSerializer


class SignUpAPI(CreateAPIView):
    """Sign up API endpoint."""

    serializer_class = UserSignUpSerializer
    queryset = CustomUser.objects.all()


class SignInAPI(ObtainAuthToken):
    """Sign in API endpoint."""

    def post(
        self: "SignInAPI", request: Request, *args: List, **kwargs: Dict
    ) -> Response:
        """Post method for SignInAPI."""
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                "token": token.key,
                "username": user.username,
            }
        )
