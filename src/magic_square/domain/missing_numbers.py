"""Missing 1..16 values — FR-03, UC-D-02."""

from __future__ import annotations

from typing import TYPE_CHECKING

from magic_square.domain.types import MissingNumbers

if TYPE_CHECKING:
    from collections.abc import Sequence


def find_missing_numbers(matrix: Sequence[Sequence[int]]) -> MissingNumbers:
    """Return the two numbers not present among non-zero cells."""
    raise NotImplementedError
