"""UI RED — PRD §8.1 Track A, DESIGN §2.3. Source: docs/PRD_magic_square_4x4_tdd.md."""

from __future__ import annotations

import pytest

from magic_square.boundary import (
    BoundaryError,
    MESSAGES,
    UI_DUPLICATE_NONZERO,
    UI_INVALID_BLANK_COUNT,
    UI_INVALID_SIZE,
    UI_OUT_OF_RANGE,
    validate_matrix_raw,
)


def test_ui_red_01_three_by_four_matrix_invalid_size() -> None:
    """UI-RED-01 — 3×4 행렬 → UI_INVALID_SIZE, 도메인 미호출(검증 선행)."""
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    with pytest.raises(BoundaryError) as exc_info:
        validate_matrix_raw(matrix)
    assert exc_info.value.code == UI_INVALID_SIZE
    assert exc_info.value.message == MESSAGES[UI_INVALID_SIZE]


def test_ui_red_02_three_blanks_invalid_blank_count() -> None:
    """UI-RED-02 — 빈칸 3개 → UI_INVALID_BLANK_COUNT."""
    matrix = [
        [0, 0, 0, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    with pytest.raises(BoundaryError) as exc_info:
        validate_matrix_raw(matrix)
    assert exc_info.value.code == UI_INVALID_BLANK_COUNT
    assert exc_info.value.message == MESSAGES[UI_INVALID_BLANK_COUNT]


def test_ui_red_03_value_out_of_range() -> None:
    """UI-RED-03 — 값 17 포함 → UI_OUT_OF_RANGE."""
    matrix = [
        [0, 0, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 17],
    ]
    with pytest.raises(BoundaryError) as exc_info:
        validate_matrix_raw(matrix)
    assert exc_info.value.code == UI_OUT_OF_RANGE
    assert exc_info.value.message == MESSAGES[UI_OUT_OF_RANGE]


def test_ui_red_04_duplicate_nonzero() -> None:
    """UI-RED-04 — 0 제외 중복 → UI_DUPLICATE_NONZERO."""
    matrix = [
        [0, 0, 5, 5],
        [6, 7, 8, 9],
        [10, 11, 12, 13],
        [14, 15, 16, 1],
    ]
    with pytest.raises(BoundaryError) as exc_info:
        validate_matrix_raw(matrix)
    assert exc_info.value.code == UI_DUPLICATE_NONZERO
    assert exc_info.value.message == MESSAGES[UI_DUPLICATE_NONZERO]


def test_ui_red_05_valid_input_mock_success_result_length_six() -> None:
    """UI-RED-05 — 유효 입력·모킹 성공 → 출력 result 길이 6 (경계 퍼사드·도메인 목)."""
    pytest.fail("RED")


def test_ui_red_06_valid_input_domain_failure_maps_ui_domain_failure() -> None:
    """UI-RED-06 — 유효 입력·도메인 실패 → UI_DOMAIN_FAILURE."""
    pytest.fail("RED")


def test_ui_red_07_success_path_result_order_matches_r1_c1_n1_r2_c2_n2() -> None:
    """UI-RED-07 — 성공 경로 → [r1,c1,n1,r2,c2,n2] 순서·값 일치."""
    pytest.fail("RED")
