"""Missing 1..16 values — FR-03, UC-D-02."""

from __future__ import annotations

from collections.abc import Sequence

from magic_square.constants import MAX_CELL_VALUE, MIN_CELL_VALUE
from magic_square.domain.errors import DOMAIN_INVALID_MISSING_COUNT, DomainError
from magic_square.domain.types import MissingNumbers


def find_missing_numbers(matrix: Sequence[Sequence[int]]) -> MissingNumbers:
    """Return the two numbers not present among non-zero cells."""
    all_values = set(range(MIN_CELL_VALUE, MAX_CELL_VALUE + 1))
    present_values = {value for row in matrix for value in row if value != 0}
    missing_values = sorted(all_values - present_values)

    if len(missing_values) != 2:
        raise DomainError(DOMAIN_INVALID_MISSING_COUNT)

    return MissingNumbers(small=missing_values[0], large=missing_values[1])
