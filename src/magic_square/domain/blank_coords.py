"""Find blank (zero) cell coordinates — FR-02, UC-D-01."""

from __future__ import annotations

from typing import TYPE_CHECKING

from magic_square.domain.types import Position

if TYPE_CHECKING:
    from collections.abc import Sequence


def find_blank_coords(matrix: Sequence[Sequence[int]]) -> tuple[Position, Position]:
    """Return two blank positions in row-major order (1-index)."""
    raise NotImplementedError
