"""Magic square predicate — FR-04 (full grid, sum 34)."""

from __future__ import annotations

from collections.abc import Sequence

from magic_square.constants import MAGIC_SUM, MATRIX_SIZE


def is_magic_square(matrix: Sequence[Sequence[int]]) -> bool:
    """True iff every row, column, and both diagonals sum to 34 (4×4, no zeros)."""
    if len(matrix) != MATRIX_SIZE or any(len(row) != MATRIX_SIZE for row in matrix):
        return False

    if any(value == 0 for row in matrix for value in row):
        return False

    for row in matrix:
        if sum(row) != MAGIC_SUM:
            return False

    for col_idx in range(MATRIX_SIZE):
        if sum(matrix[row_idx][col_idx] for row_idx in range(MATRIX_SIZE)) != MAGIC_SUM:
            return False

    primary_diag = sum(matrix[idx][idx] for idx in range(MATRIX_SIZE))
    secondary_diag = sum(matrix[idx][MATRIX_SIZE - 1 - idx] for idx in range(MATRIX_SIZE))
    return primary_diag == MAGIC_SUM and secondary_diag == MAGIC_SUM
