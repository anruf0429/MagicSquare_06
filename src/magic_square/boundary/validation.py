"""Raw matrix validation before domain entry (FR-01)."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence


def validate_matrix_raw(matrix: Sequence[Sequence[int]]) -> None:
    """Validate IC-01~04; raise BoundaryError on failure.

    Success: returns None. Failure: raises magic_square.boundary.errors.BoundaryError
    with UI_* code and PRD-fixed message.
    """
    raise NotImplementedError
