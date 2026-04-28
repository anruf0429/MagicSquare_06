# Magic Square 4x4 리팩토링 사전 분석 보고서

본 문서는 `green` 기준으로 생성한 `refactoring` 브랜치에서, 리팩토링 착수 전 수행한 사전 점검 결과를 정리한다. 범위는 `src/magic_square/boundary`, `src/magic_square/domain`, `src/magic_square/gui`이며, 코드 수정 없이 구조/품질/테스트 관점 분석만 수행했다.

| 항목 | 내용 |
|------|------|
| 보고서 버전 | 1.0 |
| 작업 상태 | 사전 분석 완료 (No Code Change) |
| 기준 브랜치 | `green` |
| 작업 브랜치 | `refactoring` |
| 원격 반영 | `origin/refactoring` 푸시 완료 |

---

## 1) 브랜치 작업 이력

- `green` 브랜치에서 `refactoring` 브랜치 생성 완료
- `refactoring` 브랜치를 원격 저장소(`origin/refactoring`)로 푸시 완료
- PR 생성용 링크 확보:
  - [https://github.com/anruf0429/MagicSquare_06/pull/new/refactoring](https://github.com/anruf0429/MagicSquare_06/pull/new/refactoring)

---

## 2) 테스트 존재 여부 및 리팩토링 전제 점검

### 2.1 현재 테스트 파일 존재 여부

다음 `test_*.py` 파일이 이미 존재함:

- `tests/domain/test_magic_square_solution.py`
- `tests/domain/test_magic_square_boundary_errors.py`
- `tests/domain/test_magic_square_validation.py`
- `tests/domain/test_magic_square_blank_coords.py`
- `tests/boundary/test_ui_red.py`
- `tests/entity/test_user.py`

### 2.2 추가 테스트 필요 구간

- `src/magic_square/gui/main_window.py` 전용 테스트 부재
- 특히 다음 메서드는 리팩토링 전 테스트 보강이 필요:
  - `_read_matrix()`
  - `_on_solve_clicked()`
  - `_on_fill_sample_clicked()`
  - `_on_clear_clicked()`

### 2.3 테스트 없이 리팩토링하면 안 되는 이유

- 테스트 안전망 없이 구조를 바꾸면 동작 변경(회귀)을 즉시 감지하기 어려워, 기능 보존 리팩토링 원칙을 보장할 수 없음.

---

## 3) 레이어(ECB) 관점 분석 결과

### 3.1 현재 역할 매핑

- `src/magic_square/boundary`
  - 외부 입력 검증 및 에러 매핑을 담당하며 Boundary 역할을 전반적으로 수행
- `src/magic_square/domain`
  - 순수 규칙(Entity 성격)과 절차 오케스트레이션(Control 성격)이 일부 혼재
- `src/magic_square/gui/main_window.py`
  - UI 구성/이벤트 처리 중심이나, 유스케이스 호출 및 결과 해석 일부를 직접 수행

### 3.2 위치 조정 권장

- `domain/solver.py`의 절차 제어 성격 로직은 `control/use_cases` 계층 분리 후보
- `boundary/solve.py`는 Boundary 입출력 변환 중심으로 축소하고, 흐름 제어는 Control 위임 권장

---

## 4) 코드 스멜 점검 결과

요청된 체크리스트(이해 어려운 이름, 중복 코드, 긴 함수, 매직 넘버, 긴 파라미터, 불필요 주석, 미사용 코드) 기준으로 문제 항목만 정리:

| 파일명 | 줄번호 | 스멜 종류 | 문제 설명 | 우선순위 |
|---|---:|---|---|---|
| `src/magic_square/boundary/matrix_validator.py` | 18-48 | 긴 함수 | 크기/빈칸/범위/중복 검증이 한 함수에 집중 | 중 |
| `src/magic_square/domain/solver.py` | 32-58 | 긴 함수 | 후보 생성/시도/판정/출력 포맷까지 단일 함수 수행 | 중 |
| `src/magic_square/gui/main_window.py` | 38-69 | 긴 함수 | UI 생성/배치/이벤트 연결이 `_build_ui()`에 집중 | 중 |
| `src/magic_square/boundary/matrix_validator.py`, `src/magic_square/domain/solver.py` | 24-48, 20-29 | 중복 코드 | 유사한 검증 로직(크기/범위/중복) 중복 구현 | 상 |
| `src/magic_square/gui/main_window.py` | 24-29, 48-49 | 매직 넘버 | 샘플 데이터 값 및 UI 숫자(예: `2`, `48`) 상수화 부족 | 하 |

---

## 5) SRP(단일 책임 원칙) 위반 후보

- `src/magic_square/boundary/solve.py:13`
  - 검증 호출 + 도메인 호출 + 예외 매핑 + 응답 포맷을 함께 담당
- `src/magic_square/boundary/matrix_validator.py:18`
  - 다중 검증 책임(크기/빈칸/범위/중복) 집약
- `src/magic_square/domain/solver.py:32`
  - 절차 제어, 후보 탐색, 결과 구성 책임 동시 보유

---

## 6) 리팩토링 우선순위 계획(요약)

| 순번 | 대상 파일 | 문제 | 적용 기법 | 우선순위 |
|---:|---|---|---|---|
| 1 | `src/magic_square/domain/solver.py` | Entity/Control 혼재, SRP 위반 | 함수 추출 + Control 계층 분리 | 상 |
| 2 | `src/magic_square/boundary/solve.py` | Boundary 과책임(오케스트레이션 포함) | Use case 인터페이스 도입 | 상 |
| 3 | `src/magic_square/boundary/matrix_validator.py` | 검증 로직 집약 | 규칙별 검증 함수 분리 | 중 |
| 4 | `src/magic_square/gui/main_window.py` | UI 빌드/이벤트 처리 집중 | UI 구성 함수 분해 | 중 |

---

## 7) 리팩토링 후 검증 가이드

### 7.1 회귀 테스트 명령어

- `pytest -q`
- `pytest -q tests/domain tests/boundary`
- GUI 테스트 추가 후: `pytest -q tests/gui/test_main_window.py`

### 7.2 외부 동작 동일성 확인

- 성공 케이스 입력 시 `result` 값/순서 동일성 확인
- 실패 케이스 입력 시 `UI_*` 코드와 메시지 동일성 확인
- GUI 경고 팝업(타이틀/본문) 및 결과 라벨 표시 동일성 확인

---

## 8) 결론

현재 코드베이스는 Boundary/Domain/UI가 기본적으로 분리되어 있으나, `domain/solver.py`와 `boundary/solve.py`를 중심으로 Control 책임이 섞여 있어 리팩토링 우선순위가 높다. 리팩토링은 반드시 GUI 테스트 보강 후 단계적으로 진행하는 것이 안전하다.

