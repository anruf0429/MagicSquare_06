"""Tests for the User entity."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

PROJECT_SRC = Path(__file__).resolve().parents[2] / "src"
if str(PROJECT_SRC) not in sys.path:
    sys.path.insert(0, str(PROJECT_SRC))

from entity.models.user import User


def test_create_user_with_valid_fields() -> None:
    """Creates a user when all required fields are valid."""
    # Arrange
    user_id = "user-001"
    username = "alice"
    email = "alice@example.com"

    # Act
    user = User(user_id=user_id, username=username, email=email)

    # Assert
    assert user.user_id == user_id
    assert user.username == username
    assert user.email == email
    assert user.preferred_square_size == 4


@pytest.mark.parametrize(
    "invalid_user_id",
    [
        "",
        "   ",
    ],
)
def test_create_user_raises_for_invalid_user_id(invalid_user_id: str) -> None:
    """Raises ValueError when user_id is empty."""
    # Arrange / Act / Assert
    with pytest.raises(ValueError, match="user_id must not be empty"):
        User(user_id=invalid_user_id, username="alice", email="alice@example.com")


@pytest.mark.parametrize(
    "invalid_username",
    [
        "",
        "  ",
    ],
)
def test_create_user_raises_for_invalid_username(invalid_username: str) -> None:
    """Raises ValueError when username is empty."""
    # Arrange / Act / Assert
    with pytest.raises(ValueError, match="username must not be empty"):
        User(
            user_id="user-001",
            username=invalid_username,
            email="alice@example.com",
        )


@pytest.mark.parametrize(
    "invalid_email",
    [
        "",
        "aliceexample.com",
        "alice@",
        "@example.com",
    ],
)
def test_create_user_raises_for_invalid_email(invalid_email: str) -> None:
    """Raises ValueError when email format is invalid."""
    # Arrange / Act / Assert
    with pytest.raises(ValueError, match="email must be a valid address"):
        User(user_id="user-001", username="alice", email=invalid_email)


def test_create_user_raises_for_unsupported_square_size() -> None:
    """Raises ValueError when preferred square size is unsupported."""
    # Arrange / Act / Assert
    with pytest.raises(ValueError, match="preferred_square_size must be 4"):
        User(
            user_id="user-001",
            username="alice",
            email="alice@example.com",
            preferred_square_size=3,
        )


def test_can_request_magic_square_returns_true_for_size_four() -> None:
    """Returns True when the requested size matches supported domain size."""
    # Arrange
    user = User(user_id="user-001", username="alice", email="alice@example.com")

    # Act
    result = user.can_request_magic_square(size=4)

    # Assert
    assert result is True


def test_can_request_magic_square_returns_false_for_other_sizes() -> None:
    """Returns False when the requested size is not supported."""
    # Arrange
    user = User(user_id="user-001", username="alice", email="alice@example.com")

    # Act
    result = user.can_request_magic_square(size=5)

    # Assert
    assert result is False
