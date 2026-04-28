# Test skeletons for RED principle
_Exported on 4/28/2026 at 14:14:09 GMT+9 from Cursor (3.2.11)_

---

**User**

레포 테스트 프레임워크 이름(JUnit 5, pytest 등)에 맞춰 파일/클래스 이름만 적은 테스트 스켈레톤(메서드 빈 본문, fail 또는 assertTrue(false) 한 줄)도 같은 RED 원칙으로만 적어봅니다.

---

**Cursor**

레포지토리의 테스트 프레임워크와 기존 테스트 구조를 확인합니다.



테스트 명세의 TC ID 패턴을 확인해 스켈레톤 이름과 맞춥니다.



이 레포는 **pytest** 기준(`tests/entity/test_user.py` 패턴)이므로, RED만 두른 스켈레톤은 아래처럼 두면 됩니다. **JUnit 5**는 비교용으로 한 블록만 둡니다.

---

## pytest (이 저장소에 맞음)

- 파일: `test_*.py`
- 함수형: `test_*`
- 클래스 묶음(선택): `Test*` + 메서드 `test_*`

의도적으로 아직 GREEN이 아니므로 본문은 **`pytest.fail("RED")`** 한 줄이면 충분합니다 (`assert False`도 동일하게 RED).

```python
# tests/domain/test_magic_square_blank_coords.py
import pytest


def test_tc_ms_a_001_find_blank_coords() -> None:
    pytest.fail("RED")


def test_tc_ms_a_002_find_blank_coords() -> None:
    pytest.fail("RED")


class TestMagicSquareValidation:
    def test_tc_ms_b_001_is_magic_square(self) -> None:
        pytest.fail("RED")
```

TC ID를 파일 단위로 나누는 예:

| 파일 | 역할(명세와 대응) |
|------|------------------|
| `test_magic_square_blank_coords.py` | TC-MS-A-* |
| `test_magic_square_validation.py` | TC-MS-B-* |
| `test_magic_square_solution.py` | TC-MS-C-* |
| `test_magic_square_boundary_errors.py` | TC-MS-D-* |

각 `test_*` 안은 **`pytest.fail("RED")` 한 줄**만 두면 RED 원칙만 만족합니다.

---

## JUnit 5 (참고 — 이름 규칙만)

- 파일: `MagicSquareBlankCoordsTest.java` 등 `*Test.java`
- 클래스: `public class MagicSquareBlankCoordsTest`
- 메서드: `@Test void tc_ms_a_001_findBlankCoords()`

```java
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.fail;

class MagicSquareBlankCoordsTest {

    @Test
    void tc_ms_a_001_findBlankCoords() {
        fail("RED");
    }
}
```

(`assertTrue(false)` 대신 JUnit 5에서는 **`fail("RED")`**가 의도가 더 분명합니다.)

---

**정리:** 이 프로젝트에서는 **`test_<역할>.py` + `test_tc_ms_*` 또는 `Test*`/`test_*` + 본문 `pytest.fail("RED")`**가 프레임워크 이름·RED 원칙과 맞습니다. 구현이 생기면 같은 이름의 테스트에서 `fail`을 제거하고 Arrange–Act–Assert로 채우면 됩니다.

---

**User**

@docs/test_case_specification_magic_square_4x4.md 를 위한 skeleton py 코드를 만들어줘

---

**Cursor**

명세 전체에서 TC ID와 구조를 추출합니다.



각 TC의 '테스트 기능' 행을 수집해 docstring에 반영합니다.



명세의 TC-MS-A~D 전부(24건)에 대해 `tests/domain/` 아래 pytest RED 스켈레톤을 추가하고, `src` 경로는 `tests/conftest.py`에서 한 번만 설정합니다.



작업 반영했습니다. `docs/test_case_specification_magic_square_4x4.md`의 **TC-MS-A~D 전부 24건**을 RED 스켈레톤으로 나눠 두었습니다.

### 추가된 파일

| 파일 | 명세 그룹 |
|------|-----------|
| `tests/conftest.py` | `src`를 `sys.path`에 넣어 도메인 구현·테스트 import를 맞춤 |
| `tests/domain/test_magic_square_blank_coords.py` | TC-MS-A-001 ~ A-005 |
| `tests/domain/test_magic_square_validation.py` | TC-MS-B-001 ~ B-005 |
| `tests/domain/test_magic_square_solution.py` | TC-MS-C-001 ~ C-008 |
| `tests/domain/test_magic_square_boundary_errors.py` | TC-MS-D-001 ~ D-006 |

각 테스트는 본문이 `pytest.fail("RED")` 한 줄이고, docstring에 TC ID와 명세의 **테스트 기능** 요약을 적었습니다.

`pytest tests/domain --co -q`로 **24개** 수집되는 것까지 확인했습니다. 지금은 RED라 전부 실패하는 것이 정상입니다. 구현을 채울 때 같은 함수 이름에 AAA/assert를 넣으면 됩니다.

참고: `tests/entity/test_user.py`는 기존처럼 자체 `sys.path` 처리가 있어서 `conftest.py`와 중복이지만, 동작에는 문제 없습니다. 나중에 엔티티 테스트만 `conftest`에 맞추고 중복을 줄일 수 있습니다.

---

**User**

@src/ 영역에 실제 코드가 구현될 구현코드를 skeleton 형식으로만 작성해줘. 이건 red 테스트를 위한거야

---

**Cursor**

`src/` 구조와 설계 문서를 확인한 뒤 도메인·경계 스켈레톤을 추가합니다.



DESIGN의 도메인 API와 경계(UI_*) 계약에 맞춰 `src/magic_square` 패키지로 스켈레톤을 추가합니다. 본문은 모두 `raise NotImplementedError`로 RED 단계에서 교체 가능하게 합니다.



`src/magic_square/` 아래에 **DESIGN §1.4 / PRD FR-01~05**에 맞춘 **스켈레톤만** 추가했습니다. 구현은 전부 `raise NotImplementedError`이고, RED에서 테스트가 이 모듈을 import·호출하면 **NotImplementedError**로 실패하도록 두었습니다 (나중에 GREEN에서 본문만 채우면 됩니다).

### 경계 (FR-01, `UI_*`)

| 파일 | 역할 |
|------|------|
| `magic_square/boundary/errors.py` | `BoundaryError`, `UI_*` 상수, `MESSAGES` (PRD 고정 문구) |
| `magic_square/boundary/validation.py` | `validate_matrix_raw(matrix)` — 스켈레톤 |
| `magic_square/boundary/__init__.py` | 위 심볼 re-export |

### 도메인 (FR-02~05, `DOMAIN_*`)

| 파일 | 역할 |
|------|------|
| `magic_square/domain/errors.py` | `DomainError`, `DOMAIN_*` 상수 |
| `magic_square/domain/types.py` | `Position`, `MissingNumbers` (frozen dataclass, 값 객체만) |
| `magic_square/domain/blank_coords.py` | `find_blank_coords` — 스켈레톤 |
| `magic_square/domain/judge.py` | `is_magic_square` — 스켈레톤 |
| `magic_square/domain/missing_numbers.py` | `find_missing_numbers` — 스켈레톤 |
| `magic_square/domain/solver.py` | `solve_two_blanks` → `list[int]` 길이 6, 실패 시 `DomainError` 전제 — 스켈레톤 |
| `magic_square/__init__.py` | 패키지 루트 |

`entity` 패키지와 동일하게 `tests/conftest.py`의 `src` 경로로 `from magic_square.domain.blank_coords import find_blank_coords` 형태로 쓰면 됩니다.  
**애플리케이션/퍼사드**(경계 검증 → 솔버 → `DOMAIN_NOT_MAGIC` → `UI_DOMAIN_FAILURE` 매핑)는 아직 넣지 않았습니다. 한 진입점이 필요하면 그때 `boundary`에 얇은 조합 모듈을 추가하면 됩니다.

---

**User**

 ### 테스트 해 보기!
1. 한 번만: 가상환경·설치
프로젝트 루트(MagicSquare )에서:

python -m venv .venv
source .venv/Scripts/activate   # PowerShell이면: .venv\Scripts\Activate.ps1
pip install -U pip
pip install -e ".[dev]"

2. 테스트 실행
전체:

cd "c:/DEV/MagicSquare _1004"
pytest

3. 커버리지
dev 옵션에는 pytest만 있고 pytest-cov는 없음이므로 커버리지 쓸 때만 추가합니다.

pip install pytest-cov
pytest --cov=magicsquare --cov-report=term-missing
pytest --cov=magicsquare --cov-report=html

생성된 htmlcov/index.html을 브라우저로 열면 됩니다.

---

**Cursor**

프로젝트 상태를 확인하고, 안내와 맞게 `pyproject.toml`과 테스트·커버리지 설정을 추가합니다.



`pyproject.toml`이 없어 `pip install -e ".[dev]"`가 동작하지 않습니다. 워크숍 절차에 맞춰 추가하고, 커버리지 대상은 실제 패키지 이름인 `magic_square`(및 `entity`)로 설정합니다.



`pyproject.toml`을 추가해 워크숍의 `pip install -e ".[dev]"`가 동작합니다. README의 옛날 “pyproject 없음” 문구를 짧게 갱신합니다.



다음을 반영했습니다.

### 1. `pyproject.toml` 추가 (`pip install -e ".[dev]"` 가능)
- **프로젝트 이름(distribution):** `magicsquare` (워크숍 문서와 동일)
- **실제 import 패키지:** `magic_square`, `entity` (`src/` 레이아웃)
- **`[project.optional-dependencies]`:** `dev` → `pytest`, `cov` → `pytest-cov`
- **`[tool.pytest.ini_options]`:** `testpaths = ["tests"]`, `pythonpath = ["src"]`
- **`[tool.coverage.run]`:** `source = ["src"]`

### 2. 워크숍 안내와 맞추려면
| 문서 예시 | 이 레포 기준 |
|-----------|----------------|
| `cd "c:/DEV/MagicSquare _1004"` | **`cd c:\DEV\MagicSquare`** (현재 워크스페이스 경로) |
| `pytest --cov=magicsquare` | **`pytest --cov=magic_square --cov=entity`** (`magicsquare`는 pip 패키지 이름이고, 커버리지는 **모듈 이름**을 씀) |

전체 테스트를 돌리면 `tests/domain` RED **24건 실패 + `tests/entity` 12건 통과**가 나오는 것이 지금 상태에서 정상입니다. GREEN 전까지는 `pytest tests/entity -q`만 보면 전부 통과합니다.

### 3. README
「pyproject 없음」 문구를 지우고, 위 가상환경·`pip install -e ".[dev]"`·커버리지 명령을 반영해 두었습니다.

로컬에서 이미 실행해 본 순서는 다음과 같습니다.

```powershell
cd c:\DEV\MagicSquare
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
.\.venv\Scripts\python.exe -m pytest -q
```

커버리지(엔티티만 예시):

```powershell
pip install pytest-cov
pytest --cov=magic_square --cov=entity --cov-report=term-missing -q tests/entity
```

---

**User**

<system_notification>
The following task has finished. If you were already aware, ignore this notification and do not restate prior responses.

<task>
kind: shell
status: success
task_id: 772629
title: Create venv and editable install with dev extras
output_path: C:\Users\usejen_id\.cursor\projects\c-DEV-MagicSquare\terminals\772629.txt
</task>
</system_notification>
<user_query>Briefly inform the user about the task result and perform any follow-up actions (if needed).</user_query>

---

**Cursor**

**결과:** 백그라운드 작업이 **성공적으로 끝났습니다.** `c:\DEV\MagicSquare`에서 `.venv`를 만들고 `pip install -e ".[dev]"`로 **magicsquare** 편집 가능 설치와 **pytest**까지 설치된 상태입니다.

**후속 조치:** 필수는 없습니다. 이어서 할 일이 있다면 예를 들면 다음 정도입니다.

- 터미널에서 `.\.venv\Scripts\Activate.ps1` 후 `pytest` 또는 `pytest tests/entity -q`
- 커버리지: `pip install pytest-cov` 후 `pytest --cov=magic_square --cov=entity ...`

(`tests/domain` RED 24건 실패는 의도된 스켈레톤 동작입니다.)

---

**User**

@report/ 에 현재까지 내용을 내보내줘

---

**Cursor**

기존 `report/` 보고서 형식과 현재 저장소 상태를 확인합니다.



`report/07` 형식에 맞춰 현재 저장소 스냅샷 보고서를 작성합니다.



`report/08_project_snapshot_export_report.md`에 **현재까지 상태**를 워크숍 보고서 형식으로 정리해 두었습니다.

### 들어 있는 내용
- **`pyproject.toml`**: 편집 가능 설치(`magicsquare`), `dev`/`cov`, pytest·coverage 설정
- **`src/magic_square/`**: boundary·domain 스켈레톤 파일 목록과 역할
- **`tests/`**: `conftest`, TC-MS RED 24건·엔티티 12건, 실행 시 기대 결과(24 fail + 12 pass)
- **문서 연계**: `report/07`, `05`, `03`, PRD/DESIGN와의 대응
- **검증 항목(VE-SN-01~04)** 및 **후속 권장**(GREEN, 퍼사드, `.gitignore`, README 표 정합)

이전 `report/01`~`07`과 같은 톤(표·절 번호·참조 경로)으로 맞춰 두었습니다.

