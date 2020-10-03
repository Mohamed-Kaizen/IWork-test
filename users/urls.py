"""Users URL Configuration."""
from django.urls import include, path

from .views import SignInAPI, SignUpAPI

urlpatterns = [
    path("register/", include("dj_rest_auth.registration.urls")),
    path("", include("dj_rest_auth.urls")),
    path("signup/", SignUpAPI.as_view()),
    path("signin/", SignInAPI.as_view()),
]
