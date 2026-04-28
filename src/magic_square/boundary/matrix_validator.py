"""Raw matrix validation before domain entry (FR-01)."""

from __future__ import annotations

from collections.abc import Sequence

from magic_square.constants import MATRIX_SIZE
from magic_square.boundary.errors import (
    MESSAGES,
    UI_DUPLICATE_NONZERO,
    UI_INVALID_BLANK_COUNT,
    UI_INVALID_SIZE,
    UI_OUT_OF_RANGE,
    BoundaryError,
)


def validate_matrix_raw(matrix: Sequence[Sequence[int]]) -> None:
    """Validate IC-01~04; raise BoundaryError on failure.

    Success: returns None. Failure: raises magic_square.boundary.errors.BoundaryError
    with UI_* code and PRD-fixed message.
    """
    # IC-01 - MATRIX_SIZE x MATRIX_SIZE
    if len(matrix) != MATRIX_SIZE:
        raise BoundaryError(UI_INVALID_SIZE, MESSAGES[UI_INVALID_SIZE])
    for row in matrix:
        if len(row) != MATRIX_SIZE:
            raise BoundaryError(UI_INVALID_SIZE, MESSAGES[UI_INVALID_SIZE])

    # IC-02 - exactly two blanks (zero values)
    blank_count = sum(1 for row in matrix for value in row if value == 0)
    if blank_count != 2:
        raise BoundaryError(
            UI_INVALID_BLANK_COUNT,
            MESSAGES[UI_INVALID_BLANK_COUNT],
        )

    # IC-03 - each cell must be 0 or in [1, 16]
    for row in matrix:
        for value in row:
            if value != 0 and not 1 <= value <= MATRIX_SIZE * MATRIX_SIZE:
                raise BoundaryError(UI_OUT_OF_RANGE, MESSAGES[UI_OUT_OF_RANGE])

    # IC-04 - non-zero values must be unique
    non_zero_values = [value for row in matrix for value in row if value != 0]
    if len(non_zero_values) != len(set(non_zero_values)):
        raise BoundaryError(UI_DUPLICATE_NONZERO, MESSAGES[UI_DUPLICATE_NONZERO])
