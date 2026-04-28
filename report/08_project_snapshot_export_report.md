# 프로젝트 현황 스냅샷 내보내기 보고서

본 문서는 Magic Square(4×4) TDD 연습 저장소에 대해 **작성 시점 기준의 코드·테스트·빌드 설정 상태**를 한 곳에 묶어 **보고서 형태로 내보낸** 것이다. 실제 도메인 솔버·경계 검증의 **GREEN 완료 여부**가 아니라, **산출물 목록·역할·실행 결과 요약**에 초점을 둔다.

| 항목 | 내용 |
|------|------|
| 보고서 버전 | 1.0 |
| 상태 | 스냅샷·내보내기 |
| 스냅샷 기준 | 워킹 트리 기준(커밋 여부와 무관); 브랜치는 저장소 클론 시점에 따름 |
| 근거 문서 | `docs/PRD_magic_square_4x4_tdd.md`(v2.1), `docs/DESIGN_layered_architecture_tdd_magic_square_4x4.md`, `docs/test_case_specification_magic_square_4x4.md`, `README.md`, `report/05_*`, `report/07_*` |

---

## 1) 작업 배경

- PRD·DESIGN·테스트 명세(`report/07`, `docs/test_case_specification_magic_square_4x4.md`)에 맞춘 **구현 착수 전후**의 저장소 상태를 문서화할 필요가 있다.
- **`pyproject.toml` 도입**, **`magic_square` 패키지 스켈레톤**, **TC-MS 대응 RED 테스트 스켈레톤**, **README 실행 안내 갱신** 등이 병렬로 진행되었으므로, 후속 리뷰·CI·교육용으로 **단일 스냅샷**을 남긴다.

---

## 2) 산출물·경로 요약

| 구분 | 경로 | 설명 (현재 역할) |
|------|------|------------------|
| 빌드·패키징 | `pyproject.toml` | 배포 이름 `magicsquare`, `src/` 레이아웃, optional-deps `dev`(pytest), `cov`(pytest-cov), `[tool.pytest.ini_options]`, `[tool.coverage.run]` |
| 도메인·경계 스켈레톤 | `src/magic_square/` | Boundary(`validate_matrix_raw`, `UI_*`·`BoundaryError`), Domain(`find_blank_coords`, `is_magic_square`, `find_missing_numbers`, `solve_two_blanks`, `DOMAIN_*`·`DomainError`, `Position`/`MissingNumbers`) — **본문은 `NotImplementedError`(RED 대비)** |
| ECB 예시 엔티티 | `src/entity/models/user.py` | Report/3 패턴의 `User` 및 검증 |
| 테스트 공통 | `tests/conftest.py` | `src`를 `sys.path`에 추가 |
| 명세 연계 RED 스켈레톤 | `tests/domain/test_magic_square_*.py` (4파일) | TC-MS-A~D **24건**, 각 `pytest.fail("RED")` |
| 엔티티 테스트 | `tests/entity/test_user.py` | AAA·pytest, **통과(구현 완료)** |
| 진입·실행 문서 | `README.md` | venv, `pip install -e ".[dev]"`, pytest·커버리지 명령(`magic_square`·`entity`), To-Do·문서 맵 |
| 본 내보내기 보고서 | `report/08_project_snapshot_export_report.md` | 본 문서 |

---

## 3) 소스 트리 (마방진 관련)

```
src/magic_square/
  __init__.py
  boundary/
    __init__.py
    errors.py          # BoundaryError, UI_* , MESSAGES
    matrix_validator.py # validate_matrix_raw → NotImplementedError
  domain/
    __init__.py
    errors.py          # DomainError, DOMAIN_*
    types.py           # Position, MissingNumbers
    blank_coords.py    # find_blank_coords → NotImplementedError
    judge.py           # is_magic_square → NotImplementedError
    missing_numbers.py # find_missing_numbers → NotImplementedError
    solver.py          # solve_two_blanks → NotImplementedError
```

---

## 4) 테스트 실행 결과 (요약)

| 대상 | 개수·결과 | 비고 |
|------|------------|------|
| `tests/entity` | 12 passed | `User` 엔티티 GREEN |
| `tests/domain` | 24 failed (`pytest.fail("RED")`) | TC-MS 스켈레톤 — **의도된 RED** |
| 전체 `pytest` | 24 failed, 12 passed | 도메인 명세 테스트가 GREEN으로 바뀔 때까지 실패가 정상 |

커버리지: `pytest-cov`로 `magic_square`·`entity` 또는 `source = ["src"]` 기준 측정 가능. PRD NFR(도메인 ≥95%, 경계 ≥85%)는 **구현 완료 후** 게이트로 적용한다.

---

## 5) 기존 보고서·문서와의 관계

| 문서 | 본 스냅샷과의 관계 |
|------|---------------------|
| `report/07_*` | TC-MS 명세 → `tests/domain` 파일·함수 이름으로 **추적 가능** |
| `report/05_*` | README가 `pyproject.toml`·venv·커버리지 안내를 포함하도록 **갱신됨**(본 스냅샷과 정합) |
| `report/03_*` | `entity`·`tests/entity`는 마방진 Epic과 분리된 **ECB 예시**로 유지 |
| `docs/PRD_*`, `docs/DESIGN_*` | `magic_square` API 이름·코드는 DESIGN §1.4·경계 `UI_*`와 **용어 정합** |

---

## 6) 검증·완료 조건 (본 스냅샷 보고서 기준)

| ID | 내용 | 상태 판단 |
|----|------|-----------|
| VE-SN-01 | `pyproject.toml` 존재, `pip install -e ".[dev]"`로 편집 가능 설치 가능 | 파일·로컬 설치 로그 |
| VE-SN-02 | `src/magic_square`에 boundary/domain 모듈이 스켈레톤으로 존재 | 트리·import |
| VE-SN-03 | `tests/domain`에 TC-MS-A~D 24개 테스트 함수 존재 | `pytest --co` |
| VE-SN-04 | README에 venv·pytest·커버리지(`magic_square`·`entity`) 안내가 있다 | README 대조 |

---

## 7) 결론 및 후속 권장

- **GREEN 단계:** `magic_square` 각 모듈에서 `NotImplementedError`를 제거하고, TC-MS별로 `tests/domain`의 `pytest.fail`을 실제 단언으로 교체한다.
- **경계 단일 진입:** 필요 시 `boundary`에서 `validate_matrix_raw` → `solve_two_blanks` 조합 및 `DOMAIN_NOT_MAGIC` → `UI_DOMAIN_FAILURE` 매핑을 **한 퍼사드**로 묶는다(DESIGN §2).
- **저장소 정리:** `.venv/`, `.coverage`, `htmlcov/`, `__pycache__/`, `*.egg-info/`는 `.gitignore`에 두고 커밋에서 제외하는 것이 일반적이다(본 보고서 작성 시 일부는 미추적 상태일 수 있음).
- **README 표:** “현재까지의 작업” 표의 **빌드 설정** 행은 `pyproject.toml` 도입 후 내용이 바뀌었으므로, 상단 스냅샷 표와 **문장 중복·모순**이 없는지 주기적으로 맞춘다.

---

## 8) 참조 파일 경로

- `pyproject.toml`
- `README.md`
- `src/magic_square/`
- `tests/conftest.py`
- `tests/domain/`
- `tests/entity/test_user.py`
- `docs/test_case_specification_magic_square_4x4.md`
- `report/07_test_case_specification_export_report.md`
