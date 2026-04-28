"""Boundary use-case orchestration for solving a two-blank matrix."""

from __future__ import annotations

from collections.abc import Sequence

from magic_square.boundary.errors import MESSAGES, UI_DOMAIN_FAILURE, BoundaryError
from magic_square.boundary.matrix_validator import validate_matrix_raw
from magic_square.domain.errors import DOMAIN_NOT_MAGIC, DomainError
from magic_square.domain.solver import solve_two_blanks


def solve_matrix(matrix: Sequence[Sequence[int]]) -> dict[str, list[int]]:
    """Validate raw input, delegate domain solving, and map boundary failures."""
    validate_matrix_raw(matrix)
    try:
        result = solve_two_blanks(matrix)
    except DomainError as exc:
        if exc.code == DOMAIN_NOT_MAGIC:
            raise BoundaryError(UI_DOMAIN_FAILURE, MESSAGES[UI_DOMAIN_FAILURE]) from exc
        raise
    return {"result": result}
