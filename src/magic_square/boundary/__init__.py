"""Input validation (FR-01) — maps to UI_* codes and fixed messages."""

from __future__ import annotations

from magic_square.boundary.errors import (
    MESSAGES,
    UI_DOMAIN_FAILURE,
    UI_DUPLICATE_NONZERO,
    UI_INVALID_BLANK_COUNT,
    UI_INVALID_SIZE,
    UI_OUT_OF_RANGE,
    BoundaryError,
)
from magic_square.boundary.validation import validate_matrix_raw

__all__ = [
    "MESSAGES",
    "UI_DOMAIN_FAILURE",
    "UI_DUPLICATE_NONZERO",
    "UI_INVALID_BLANK_COUNT",
    "UI_INVALID_SIZE",
    "UI_OUT_OF_RANGE",
    "BoundaryError",
    "validate_matrix_raw",
]
