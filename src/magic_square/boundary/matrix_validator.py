"""Raw matrix validation before domain entry (FR-01)."""

from __future__ import annotations

from collections.abc import Sequence

from magic_square.boundary.errors import (
    MESSAGES,
    UI_INVALID_SIZE,
    BoundaryError,
)


def validate_matrix_raw(matrix: Sequence[Sequence[int]]) -> None:
    """Validate IC-01~04; raise BoundaryError on failure.

    Success: returns None. Failure: raises magic_square.boundary.errors.BoundaryError
    with UI_* code and PRD-fixed message.
    """
    # IC-01 - 4x4
    if len(matrix) != 4:
        raise BoundaryError(UI_INVALID_SIZE, MESSAGES[UI_INVALID_SIZE])
    for row in matrix:
        if len(row) != 4:
            raise BoundaryError(UI_INVALID_SIZE, MESSAGES[UI_INVALID_SIZE])

    # IC-02~04 - UI-RED-02~04 (pending)
    raise NotImplementedError
