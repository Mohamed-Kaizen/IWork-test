"""Collection of test for users views."""
from typing import Any, Dict

import pytest
from django.test import Client


@pytest.fixture
def user_creation_data() -> Dict:
    """A fixture for user creation."""
    return {
        "username": "iwork",
        "password": "123456789iwork",
        "email": "iwork@iwork.com",
        "full_name": "iwork",
    }


@pytest.mark.django_db
def test_sign_up(client: Client, user_creation_data: Dict) -> None:
    """Test for sign up endpoint."""
    response = client.post(
        "/api/users/signup/",
        user_creation_data,
    )
    assert response.status_code == 201


@pytest.mark.django_db
def test_sign_in(
    client: Client, django_user_model: Any, user_creation_data: Dict
) -> None:
    """Test for sign in endpoint."""
    django_user_model.objects.create_user(**user_creation_data)
    response = client.post(
        "/api/users/signin/",
        "username=iwork&password=123456789iwork",
        "application/x-www-form-urlencoded",
    )
    assert response.status_code == 200
