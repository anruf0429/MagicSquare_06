"""RED skeleton — TC-MS-B. Source: docs/test_case_specification_magic_square_4x4.md"""

from __future__ import annotations

from magic_square.domain.judge import is_magic_square


def test_tc_ms_b_001() -> None:
    """TC-MS-B-001 — 완성된 4x4 마방진은 True."""
    matrix = [
        [16, 3, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 1],
    ]
    assert is_magic_square(matrix) is True


def test_tc_ms_b_002() -> None:
    """TC-MS-B-002 — 행 합이 34가 아니면 False."""
    matrix = [
        [16, 3, 2, 12],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 1],
    ]
    assert is_magic_square(matrix) is False


def test_tc_ms_b_003() -> None:
    """TC-MS-B-003 — 열 합이 34가 아니면 False."""
    matrix = [
        [16, 3, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [5, 15, 14, 1],
    ]
    assert is_magic_square(matrix) is False


def test_tc_ms_b_004() -> None:
    """TC-MS-B-004 — 대각선 합이 깨지면 False."""
    matrix = [
        [16, 3, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 6, 12],
        [4, 15, 14, 1],
    ]
    assert is_magic_square(matrix) is False


def test_tc_ms_b_005() -> None:
    """TC-MS-B-005 — 빈칸(0)이 있으면 False."""
    matrix = [
        [16, 3, 2, 13],
        [5, 10, 11, 8],
        [9, 0, 7, 12],
        [4, 15, 14, 1],
    ]
    assert is_magic_square(matrix) is False
