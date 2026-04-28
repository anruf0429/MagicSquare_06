"""RED skeleton — TC-MS-C. Source: docs/test_case_specification_magic_square_4x4.md"""

from __future__ import annotations

import pytest

from magic_square.constants import MAGIC_SUM, MATRIX_SIZE
from magic_square.domain.errors import DOMAIN_NOT_MAGIC, DomainError
from magic_square.domain.solver import solve_two_blanks


def _apply_result(matrix: list[list[int]], result: list[int]) -> list[list[int]]:
    filled = [row[:] for row in matrix]
    r1, c1, n1, r2, c2, n2 = result
    filled[r1 - 1][c1 - 1] = n1
    filled[r2 - 1][c2 - 1] = n2
    return filled


def test_tc_ms_c_001() -> None:
    """TC-MS-C-001 — 빈칸 채우기 / 해 도출 (solution)."""
    matrix = [
        [16, 0, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [0, 15, 14, 1],
    ]
    result = solve_two_blanks(matrix)
    assert len(result) == 6


def test_tc_ms_c_002() -> None:
    """TC-MS-C-002 — 빈칸 채우기 / 해 도출 (solution)."""
    matrix = [
        [16, 0, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [0, 15, 14, 4],
    ]
    with pytest.raises(DomainError) as exc_info:
        solve_two_blanks(matrix)
    assert exc_info.value.code == DOMAIN_NOT_MAGIC


def test_tc_ms_c_003() -> None:
    """TC-MS-C-003 — 빈칸 채우기 / 해 도출 (solution)."""
    matrix = [
        [16, 0, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [0, 15, 14, 1],
    ]
    result = solve_two_blanks(matrix)
    assert result[:2] == [1, 2]
    assert result[3:5] == [4, 1]


def test_tc_ms_c_004() -> None:
    """TC-MS-C-004 — 경계값 — 최소값 1 포함."""
    matrix = [
        [16, 0, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 0],
    ]
    result = solve_two_blanks(matrix)
    assert 1 in (result[2], result[5])


def test_tc_ms_c_005() -> None:
    """TC-MS-C-005 — 경계값 — 최대값 16 포함."""
    matrix = [
        [0, 3, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 0],
    ]
    result = solve_two_blanks(matrix)
    assert 16 in (result[2], result[5])


def test_tc_ms_c_006() -> None:
    """TC-MS-C-006 — 마방진 상수(34) — 모든 행."""
    matrix = [
        [16, 0, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [0, 15, 14, 1],
    ]
    filled = _apply_result(matrix, solve_two_blanks(matrix))
    assert all(sum(row) == MAGIC_SUM for row in filled)


def test_tc_ms_c_007() -> None:
    """TC-MS-C-007 — 마방진 상수(34) — 모든 열."""
    matrix = [
        [16, 0, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [0, 15, 14, 1],
    ]
    filled = _apply_result(matrix, solve_two_blanks(matrix))
    assert all(
        sum(filled[row_idx][col_idx] for row_idx in range(MATRIX_SIZE)) == MAGIC_SUM
        for col_idx in range(MATRIX_SIZE)
    )


def test_tc_ms_c_008() -> None:
    """TC-MS-C-008 — 마방진 상수(34) — 두 대각선."""
    matrix = [
        [16, 0, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [0, 15, 14, 1],
    ]
    filled = _apply_result(matrix, solve_two_blanks(matrix))
    primary = sum(filled[idx][idx] for idx in range(MATRIX_SIZE))
    secondary = sum(filled[idx][MATRIX_SIZE - 1 - idx] for idx in range(MATRIX_SIZE))
    assert primary == MAGIC_SUM
    assert secondary == MAGIC_SUM
