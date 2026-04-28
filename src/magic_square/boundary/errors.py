"""Boundary failure type and UI_* codes (DESIGN §2.2, PRD FR-01)."""

from __future__ import annotations


class BoundaryError(Exception):
    """Raised when raw input fails FR-01 / IC-01~04."""

    __slots__ = ("code", "message")

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        self.message = message
        super().__init__(f"{code}: {message}")


UI_INVALID_SIZE = "UI_INVALID_SIZE"
UI_INVALID_BLANK_COUNT = "UI_INVALID_BLANK_COUNT"
UI_OUT_OF_RANGE = "UI_OUT_OF_RANGE"
UI_DUPLICATE_NONZERO = "UI_DUPLICATE_NONZERO"
UI_DOMAIN_FAILURE = "UI_DOMAIN_FAILURE"

MESSAGES: dict[str, str] = {
    UI_INVALID_SIZE: "matrix must be 4x4",
    UI_INVALID_BLANK_COUNT: "matrix must contain exactly two zeros",
    UI_OUT_OF_RANGE: "values must be 0 or in [1,16]",
    UI_DUPLICATE_NONZERO: "non-zero values must be unique",
    UI_DOMAIN_FAILURE: "no valid magic-square completion found",
}
