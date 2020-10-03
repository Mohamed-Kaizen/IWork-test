"""Collection of test for product views."""
from typing import Any

import pytest
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from ..models import Item


@pytest.fixture
def api_client() -> APIClient:
    """A fixture for drf."""
    return APIClient()


@pytest.fixture
def get_or_create_token(django_user_model: Any) -> Token:
    """A fixture for token."""
    user = django_user_model.objects.create_user(
        **{
            "username": "iwork",
            "password": "123456789iwork",
            "email": "iwork@iwork.com",
            "full_name": "iwork",
        }
    )
    token, _ = Token.objects.get_or_create(user=user)
    return token


@pytest.fixture
def create_item() -> str:
    """A fixture for item."""
    item = Item.objects.create(name="sdsad", quantity=4545)
    return item.slug


@pytest.mark.django_db
def test_create_item(api_client: APIClient, get_or_create_token: Token) -> None:
    """Test for create item endpoint."""
    token = get_or_create_token
    api_client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
    response = api_client.post("/api/products/", {"name": "sdsad", "quantity": 4545})
    assert response.status_code == 201


@pytest.mark.django_db
def test_item_detail(
    api_client: APIClient, create_item: str, get_or_create_token: Token
) -> None:
    """Test for item detail endpoint."""
    slug = create_item
    token = get_or_create_token
    api_client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
    response = api_client.get(f"/api/products/{slug}/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_item_update(
    api_client: APIClient, create_item: str, get_or_create_token: Token
) -> None:
    """Test for item update endpoint."""
    slug = create_item
    token = get_or_create_token
    api_client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
    response = api_client.patch(f"/api/products/{slug}/", {"quantity": 1000})
    assert response.status_code == 200


@pytest.mark.django_db
def test_item_delete(
    api_client: APIClient, create_item: str, get_or_create_token: Token
) -> None:
    """Test for item delete endpoint."""
    slug = create_item
    token = get_or_create_token
    api_client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
    response = api_client.delete(f"/api/products/{slug}/")
    assert response.status_code == 204
