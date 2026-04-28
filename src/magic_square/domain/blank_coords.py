"""Find blank (zero) cell coordinates — FR-02, UC-D-01."""

from __future__ import annotations

from typing import TYPE_CHECKING

from magic_square.domain.errors import DOMAIN_INVALID_BLANK_COUNT, DomainError
from magic_square.domain.types import Position

if TYPE_CHECKING:
    from collections.abc import Sequence


def find_blank_coords(matrix: Sequence[Sequence[int]]) -> tuple[Position, Position]:
    """Return two blank positions in row-major order (1-index)."""
    blanks: list[Position] = []
    for row_idx, row in enumerate(matrix, start=1):
        for col_idx, value in enumerate(row, start=1):
            if value == 0:
                blanks.append(Position(row=row_idx, col=col_idx))

    if len(blanks) != 2:
        raise DomainError(DOMAIN_INVALID_BLANK_COUNT)

    return blanks[0], blanks[1]
