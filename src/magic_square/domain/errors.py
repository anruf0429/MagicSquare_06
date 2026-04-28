"""Domain failure codes (DESIGN INV / §1.4) and DomainError."""

from __future__ import annotations


class DomainError(Exception):
    """Raised when domain invariants fail or no solution exists."""

    __slots__ = ("code",)

    def __init__(self, code: str) -> None:
        self.code = code
        super().__init__(code)


DOMAIN_INVALID_SIZE = "DOMAIN_INVALID_SIZE"
DOMAIN_INVALID_BLANK_COUNT = "DOMAIN_INVALID_BLANK_COUNT"
DOMAIN_OUT_OF_RANGE = "DOMAIN_OUT_OF_RANGE"
DOMAIN_DUPLICATE_NONZERO = "DOMAIN_DUPLICATE_NONZERO"
DOMAIN_INVALID_MISSING_COUNT = "DOMAIN_INVALID_MISSING_COUNT"
DOMAIN_NOT_MAGIC = "DOMAIN_NOT_MAGIC"
