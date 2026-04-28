"""Magic square predicate — FR-04 (full grid, sum 34)."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence


def is_magic_square(matrix: Sequence[Sequence[int]]) -> bool:
    """True iff every row, column, and both diagonals sum to 34 (4×4, no zeros)."""
    raise NotImplementedError
