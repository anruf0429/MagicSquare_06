"""RED skeleton — TC-MS-D. Source: docs/test_case_specification_magic_square_4x4.md"""

from __future__ import annotations

import pytest

from magic_square.domain.errors import (
    DOMAIN_DUPLICATE_NONZERO,
    DOMAIN_INVALID_SIZE,
    DOMAIN_OUT_OF_RANGE,
    DomainError,
)
from magic_square.domain.solver import solve_two_blanks


def test_tc_ms_d_001() -> None:
    """TC-MS-D-001 — 오류·예외 — 범위 밖 값."""
    matrix = [
        [16, 0, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [0, 15, 14, 17],
    ]
    with pytest.raises(DomainError) as exc_info:
        solve_two_blanks(matrix)
    assert exc_info.value.code == DOMAIN_OUT_OF_RANGE


def test_tc_ms_d_002() -> None:
    """TC-MS-D-002 — 오류·예외 — 중복."""
    matrix = [
        [16, 0, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [0, 15, 14, 16],
    ]
    with pytest.raises(DomainError) as exc_info:
        solve_two_blanks(matrix)
    assert exc_info.value.code == DOMAIN_DUPLICATE_NONZERO


def test_tc_ms_d_003() -> None:
    """TC-MS-D-003 — 오류·예외 — 크기 불일치."""
    matrix = [
        [16, 0, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
    ]
    with pytest.raises(DomainError) as exc_info:
        solve_two_blanks(matrix)
    assert exc_info.value.code == DOMAIN_INVALID_SIZE


def test_tc_ms_d_004() -> None:
    """TC-MS-D-004 — 오류·예외 — None / 빈 입력."""
    with pytest.raises(TypeError):
        solve_two_blanks(None)  # type: ignore[arg-type]


def test_tc_ms_d_005() -> None:
    """TC-MS-D-005 — 오류·예외 — 문자열 혼입."""
    matrix = [
        [16, 0, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [0, 15, 14, "x"],  # type: ignore[list-item]
    ]
    with pytest.raises(TypeError):
        solve_two_blanks(matrix)  # type: ignore[arg-type]


def test_tc_ms_d_006() -> None:
    """TC-MS-D-006 — 오류·예외 — 행 길이 불균일."""
    matrix = [
        [16, 0, 2, 13],
        [5, 10, 11],
        [9, 6, 7, 12],
        [0, 15, 14, 1],
    ]
    with pytest.raises(DomainError) as exc_info:
        solve_two_blanks(matrix)
    assert exc_info.value.code == DOMAIN_INVALID_SIZE
