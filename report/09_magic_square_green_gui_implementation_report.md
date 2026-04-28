# Magic Square 4x4 GREEN + GUI 구현 보고서

본 문서는 Magic Square(4x4) 프로젝트에서 RED 스켈레톤 상태를 GREEN으로 전환하고, 실행 가능한 PyQt6 GUI 진입점을 추가한 작업 내역을 정리한다. 목표는 (1) 도메인/경계 핵심 규칙 구현, (2) 테스트 스위트 전체 통과, (3) 단일 실행 경로(`python -m magic_square`) 확보이다.

| 항목 | 내용 |
|------|------|
| 보고서 버전 | 1.0 |
| 작업 상태 | GREEN 구현 + GUI 실행 가능 |
| 기준 브랜치 | `green` |
| 핵심 결과 | `pytest tests` 전체 통과(43 passed), PyQt6 GUI 실행 확인 |

---

## 1) 이번 작업의 목표

- RED 상태로 남아 있던 `magic_square` 도메인/경계 구현을 명세(PRD/DESIGN)에 맞춰 GREEN으로 전환한다.
- `tests/domain`, `tests/boundary`의 `pytest.fail("RED")` 스켈레톤을 실제 검증 테스트로 치환한다.
- Screen 레이어(Python Qt)를 별도 패키지(`src/magic_square/gui`)로 분리하고, 공식 실행 경로를 1개로 고정한다.

---

## 2) 구현 변경 요약

### 2.1 공통 상수 도입

- 파일: `src/magic_square/constants.py`
- 추가 상수:
  - `MATRIX_SIZE = 4`
  - `MAGIC_SUM = 34`
  - `MIN_CELL_VALUE = 1`
  - `MAX_CELL_VALUE = 16`

하드코딩된 크기/합/범위를 줄이고 Boundary·Domain·GUI에서 동일 기준을 사용하도록 정리했다.

### 2.2 Boundary (UI 계약) 구현

- 파일: `src/magic_square/boundary/matrix_validator.py`
  - IC-01~04 검증 구현:
    - 4x4 크기
    - 빈칸(0) 정확히 2개
    - 값 범위(0 또는 1~16)
    - 0 제외 중복 금지
  - 실패 시 `BoundaryError` + `UI_*` + 고정 메시지 매핑

- 파일: `src/magic_square/boundary/solve.py` (신규)
  - `solve_matrix(matrix)` 구현:
    - `validate_matrix_raw` 호출
    - `solve_two_blanks` 위임
    - `DOMAIN_NOT_MAGIC` -> `UI_DOMAIN_FAILURE`로 변환

- 파일: `src/magic_square/boundary/__init__.py`
  - `solve_matrix` re-export 추가

### 2.3 Domain (Logic 규칙) 구현

- 파일: `src/magic_square/domain/blank_coords.py`
  - row-major로 빈칸 좌표 2개를 1-index로 반환
  - 빈칸 개수 불일치 시 `DOMAIN_INVALID_BLANK_COUNT`

- 파일: `src/magic_square/domain/missing_numbers.py`
  - 1..16 중 미등장 숫자 2개를 `MissingNumbers(small, large)`로 반환
  - 개수 불일치 시 `DOMAIN_INVALID_MISSING_COUNT`

- 파일: `src/magic_square/domain/judge.py`
  - 행/열/두 대각선 합 34 여부 판정
  - 0 포함 또는 크기 불일치 입력은 `False`

- 파일: `src/magic_square/domain/solver.py`
  - 사전 검증(크기/범위/중복)
  - 두 조합 시도:
    1. `small -> first blank`, `large -> second blank`
    2. 역배치
  - 성공 시 `[r1,c1,n1,r2,c2,n2]` 반환
  - 둘 다 실패 시 `DOMAIN_NOT_MAGIC`

---

## 3) 테스트 전환(RED -> GREEN)

다음 테스트 파일의 RED 스켈레톤을 실제 검증형 테스트로 교체했다.

- `tests/boundary/test_ui_red.py`
  - UI-RED-01~07 전체 구현/통과
  - 성공 스키마(`result` 길이 6), 도메인 실패 매핑(`UI_DOMAIN_FAILURE`) 검증 포함

- `tests/domain/test_magic_square_blank_coords.py`
  - A-001~005 구현/통과

- `tests/domain/test_magic_square_validation.py`
  - B-001~005 구현/통과

- `tests/domain/test_magic_square_boundary_errors.py`
  - D-001~006 구현/통과

- `tests/domain/test_magic_square_solution.py`
  - C-001~008 구현/통과

---

## 4) GUI 실행 가능화

### 4.1 의존성 및 진입점

- 파일: `pyproject.toml`
  - optional dependency 추가: `gui = ["PyQt6"]`

- 파일: `src/magic_square/__main__.py` (신규)
  - 공식 단일 실행 경로 연결

- 파일: `src/magic_square/gui/__main__.py` (신규)
  - Qt 앱 부팅 (`QApplication`, `MainWindow`)

### 4.2 Screen 레이어 구현

- 파일: `src/magic_square/gui/main_window.py` (신규)
  - 4x4 입력 그리드(`QLineEdit`)
  - 버튼:
    - `샘플 채우기`
    - `초기화`
    - `풀기`
  - 성공 시 결과 라벨 표시
  - 입력 오류/경계 오류는 메시지 박스로 안내

### 4.3 문서 갱신

- 파일: `README.md`
  - GUI 설치/실행 명령 추가:
    - `pip install -e ".[gui]"`
    - `python -m magic_square`

---

## 5) 검증 결과

| 검증 항목 | 결과 |
|-----------|------|
| 전체 테스트 | `43 passed` |
| 명령 | `python -m pytest tests -q` |
| GUI 의존성 설치 | `pip install -e ".[gui]"` 성공 |
| GUI 모듈 import | `from magic_square.gui.main_window import MainWindow` 성공 |
| GUI 실행 | `python -m magic_square` 실행 확인 |

---

## 6) 변경 파일 목록(요약)

### 신규

- `src/magic_square/constants.py`
- `src/magic_square/boundary/solve.py`
- `src/magic_square/gui/__init__.py`
- `src/magic_square/gui/__main__.py`
- `src/magic_square/gui/main_window.py`
- `src/magic_square/__main__.py`
- `report/09_magic_square_green_gui_implementation_report.md`

### 수정

- `src/magic_square/boundary/__init__.py`
- `src/magic_square/boundary/matrix_validator.py`
- `src/magic_square/domain/blank_coords.py`
- `src/magic_square/domain/judge.py`
- `src/magic_square/domain/missing_numbers.py`
- `src/magic_square/domain/solver.py`
- `tests/boundary/test_ui_red.py`
- `tests/domain/test_magic_square_blank_coords.py`
- `tests/domain/test_magic_square_boundary_errors.py`
- `tests/domain/test_magic_square_solution.py`
- `tests/domain/test_magic_square_validation.py`
- `pyproject.toml`
- `README.md`

---

## 7) 결론

이번 작업으로 Magic Square 프로젝트는 RED 스켈레톤 단계에서 벗어나, 경계/도메인 핵심 규칙과 테스트가 모두 Green 상태가 되었다. 또한 PyQt6 기반 Screen 레이어를 별도 패키지로 분리해 실행 가능한 MVP GUI를 확보했으며, 공식 실행 경로를 `python -m magic_square`로 통일했다.

