"""User entity for the MagicSquare domain."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    """Represents a domain user interacting with MagicSquare use cases.

    Attributes:
        user_id: Unique identifier for the user.
        username: Display name used in the application.
        email: Contact email address.
        preferred_square_size: Preferred magic square size. MagicSquare currently
            supports only 4x4.
    """

    user_id: str
    username: str
    email: str
    preferred_square_size: int = 4

    def __post_init__(self) -> None:
        """Validates user invariants at creation time."""
        self._validate_non_empty("user_id", self.user_id)
        self._validate_non_empty("username", self.username)
        self._validate_email(self.email)
        self._validate_square_size(self.preferred_square_size)

    def can_request_magic_square(self, size: int) -> bool:
        """Checks whether the user can request a magic square for the size.

        Args:
            size: Target magic square size.

        Returns:
            True when the requested size is supported by the domain.
        """
        return size == self.preferred_square_size == 4

    @staticmethod
    def _validate_non_empty(field_name: str, value: str) -> None:
        """Ensures the field value is not empty or blank.

        Args:
            field_name: Name of the validated field.
            value: Field value to validate.

        Raises:
            ValueError: If value is empty or blank.
        """
        if not value or not value.strip():
            raise ValueError(f"{field_name} must not be empty")

    @staticmethod
    def _validate_email(email: str) -> None:
        """Ensures the email contains a basic address structure.

        Args:
            email: Email value to validate.

        Raises:
            ValueError: If email format is invalid.
        """
        if "@" not in email:
            raise ValueError("email must be a valid address")

        local_part, _, domain_part = email.partition("@")
        if not local_part or not domain_part:
            raise ValueError("email must be a valid address")

    @staticmethod
    def _validate_square_size(size: int) -> None:
        """Ensures preferred square size is supported by MagicSquare.

        Args:
            size: Preferred square size.

        Raises:
            ValueError: If size is not 4.
        """
        if size != 4:
            raise ValueError("preferred_square_size must be 4")
