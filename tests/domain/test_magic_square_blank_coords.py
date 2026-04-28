"""RED skeleton — TC-MS-A. Source: docs/test_case_specification_magic_square_4x4.md"""

from __future__ import annotations

import pytest

from magic_square.domain.blank_coords import find_blank_coords
from magic_square.domain.errors import DOMAIN_INVALID_BLANK_COUNT, DomainError
from magic_square.domain.types import Position


def test_tc_ms_a_001() -> None:
    """TC-MS-A-001 — row-major 순서로 빈칸 좌표 2개를 반환한다."""
    matrix = [
        [16, 2, 3, 0],
        [5, 11, 10, 8],
        [9, 7, 6, 12],
        [0, 14, 15, 1],
    ]
    first, second = find_blank_coords(matrix)
    assert first == Position(row=1, col=4)
    assert second == Position(row=4, col=1)


def test_tc_ms_a_002() -> None:
    """TC-MS-A-002 — 빈칸이 2개가 아니면 DOMAIN_INVALID_BLANK_COUNT."""
    matrix = [
        [16, 2, 3, 4],
        [5, 11, 10, 8],
        [9, 7, 6, 12],
        [0, 14, 15, 1],
    ]
    with pytest.raises(DomainError) as exc_info:
        find_blank_coords(matrix)
    assert exc_info.value.code == DOMAIN_INVALID_BLANK_COUNT


def test_tc_ms_a_003() -> None:
    """TC-MS-A-003 — 빈칸 3개면 DOMAIN_INVALID_BLANK_COUNT."""
    matrix = [
        [16, 0, 3, 0],
        [5, 11, 10, 8],
        [9, 7, 6, 12],
        [0, 14, 15, 1],
    ]
    with pytest.raises(DomainError) as exc_info:
        find_blank_coords(matrix)
    assert exc_info.value.code == DOMAIN_INVALID_BLANK_COUNT


def test_tc_ms_a_004() -> None:
    """TC-MS-A-004 — 1-index 좌표를 반환한다."""
    matrix = [
        [0, 2, 3, 4],
        [5, 11, 10, 8],
        [9, 7, 6, 12],
        [13, 14, 0, 1],
    ]
    first, second = find_blank_coords(matrix)
    assert first == Position(row=1, col=1)
    assert second == Position(row=4, col=3)


def test_tc_ms_a_005() -> None:
    """TC-MS-A-005 — row-major에서 먼저 발견한 빈칸이 first다."""
    matrix = [
        [16, 2, 3, 4],
        [5, 0, 10, 8],
        [9, 7, 6, 0],
        [13, 14, 15, 1],
    ]
    first, second = find_blank_coords(matrix)
    assert first == Position(row=2, col=2)
    assert second == Position(row=3, col=4)
