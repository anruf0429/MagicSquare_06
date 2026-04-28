"""Two-blank completion — FR-05, DESIGN OC-01~09."""

from __future__ import annotations

from collections.abc import Sequence

from magic_square.constants import MATRIX_SIZE, MAX_CELL_VALUE, MIN_CELL_VALUE
from magic_square.domain.blank_coords import find_blank_coords
from magic_square.domain.errors import (
    DOMAIN_DUPLICATE_NONZERO,
    DOMAIN_INVALID_SIZE,
    DOMAIN_NOT_MAGIC,
    DOMAIN_OUT_OF_RANGE,
    DomainError,
)
from magic_square.domain.judge import is_magic_square
from magic_square.domain.missing_numbers import find_missing_numbers


def _validate_matrix(matrix: Sequence[Sequence[int]]) -> None:
    if len(matrix) != MATRIX_SIZE or any(len(row) != MATRIX_SIZE for row in matrix):
        raise DomainError(DOMAIN_INVALID_SIZE)

    non_zero_values = [value for row in matrix for value in row if value != 0]
    if any(value < MIN_CELL_VALUE or value > MAX_CELL_VALUE for value in non_zero_values):
        raise DomainError(DOMAIN_OUT_OF_RANGE)

    if len(non_zero_values) != len(set(non_zero_values)):
        raise DomainError(DOMAIN_DUPLICATE_NONZERO)


def solve_two_blanks(matrix: Sequence[Sequence[int]]) -> list[int]:
    """Return ``[r1,c1,n1,r2,c2,n2]`` (1-index coords) or raise DomainError."""
    _validate_matrix(matrix)

    first_blank, second_blank = find_blank_coords(matrix)
    missing = find_missing_numbers(matrix)

    candidates = [
        (missing.small, missing.large),
        (missing.large, missing.small),
    ]

    for first_value, second_value in candidates:
        trial = [list(row) for row in matrix]
        trial[first_blank.row - 1][first_blank.col - 1] = first_value
        trial[second_blank.row - 1][second_blank.col - 1] = second_value
        if is_magic_square(trial):
            return [
                first_blank.row,
                first_blank.col,
                first_value,
                second_blank.row,
                second_blank.col,
                second_value,
            ]

    raise DomainError(DOMAIN_NOT_MAGIC)
