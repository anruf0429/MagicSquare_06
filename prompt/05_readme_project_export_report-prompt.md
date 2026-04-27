# To-do list creation references
_Exported on 4/28/2026 at 08:32:03 GMT+9 from Cursor (3.2.11)_

---

**User**

Ｔｏ－Ｄｏ　리스트를 작성하고 싶습니다. 작성한 문서 중 무엇을 참조해서 만들어야 할까요?

---

**Cursor**

프로젝트 문서를 확인해 To-Do 리스트 작성 시 참조 우선순위를 제안합니다.



To-Do 리스트를 **무엇을 해야 하는지(우선순위·완료 조건)** 기준으로 잡으려면 아래처럼 참조하면 됩니다.

## 1순위: `docs/PRD_magic_square_4x4_tdd.md`

- **범위**: In-Scope / Out-of-Scope(§4)로 “할 일 / 하지 말 일”을 나눕니다.
- **작업 단위**: **FR-01, FR-02, …** 기능 요구와 각각의 **AC(승인 기준)**가 테스트·체크리스트로 바로 붙습니다.
- **비즈니스 규칙·계약**: PRD 본문과 §6 등에 고정된 입력·출력·오류 의미가 정리되어 있습니다.

구현 To-Do의 **주 소스**는 이 PRD가 맞습니다.

## 2순위: `docs/DESIGN_layered_architecture_tdd_magic_square_4x4.md`

- PRD를 **레이어·컴포넌트·순서**로 쪼갤 때 씁니다 (경계 vs 도메인, `BlankFinder` 같은 논리 이름, IC/OC 계약).
- “어떤 클래스/서비스부터 테스트할지” 같은 **구조·순서 To-Do**는 여기를 함께 보면 됩니다.

## 3순위: `report/` 보고서들

PRD 표에도 나오듯 **근거·패턴**용입니다.

- **01 / 02**: 문제 정의, Dual-Track TDD·경계 코드·메시지 테이블 등 **이미 정해진 용어·에러 코드**를 맞출 때.
- **03** (`03_user_entity_ecb_tdd_implementation_report.md`): **User 엔티티 ECB + TDD** 절차를 이 프로젝트와 같은 방식으로 맞추고 싶을 때 “진행 방식” 참고용입니다. 마방진 **기능 목록**의 원천은 PRD가 아니라 이 보고서입니다.

---

**요약**: To-Do의 **항목과 완료 조건**은 **`docs/PRD_magic_square_4x4_tdd.md`**를 기준으로 세우고, **실행 순서·레이어·계약 세부**는 **`docs/DESIGN_layered_architecture_tdd_magic_square_4x4.md`**를 보완 참고하며, **스타일·리포트와의 추적**은 **`report/02`·`03`**을 필요할 때만 열면 됩니다.

---

**User**

당신은 시니어 소프트웨어 아키텍트이자 TDD 코치입니다. 할 일 목록의 항목과 완료 조건은 docs/5.PRD_MagicSquare_4x4_TDD.md를 주 소스로 두고, 스토리 단위 분해는 Report/4, 계약·오류 세부는 Report/2, 품질·TDD·ECB 준수는 Report/3와 Cursor 규칙을 참조해,

다음 방법론을 적용하여 "Magic Square 4x4 완성 시스템"의 구현용 To-Do 구조를 작성하세요.

적용 방법론:

Concept-to-Code Traceability
Dual-Track UI + Logic TDD
To-Do → Scenario → Test → Code 구조
ECB(Entity / Control / Boundary) 모델
RED → GREEN → REFACTOR
반드시 한국어로 작성하세요.

[시스템 목표] 부분적으로 비어 있는 4x4 Magic Square를 완성하는 시스템의 개발 To-Do를 작성합니다.

[도메인 규칙]

보드는 4x4이다.
숫자는 1~16만 사용한다.
0은 빈칸이다.
정확히 2칸이 비어 있다.
0을 제외한 중복 숫자는 허용되지 않는다.
모든 행, 열, 대각선의 합은 34여야 한다.
해결 가능한 경우 빈칸 값을 찾아 채운다.
유효하지 않은 보드는 거부한다.
[출력 형식] 다음 구조를 반드시 지켜서 작성하세요.

Epic
User Story
Phase별 Task 목록
각 Task에는 반드시 아래 정보를 포함하세요.
Task ID
RED / GREEN / REFACTOR 여부
작업 제목
Scenario Level (L0/L1/L2/L3)
연결되는 Test 이름
연결되는 Code 대상
ECB 스테레오타입 (Entity / Control / Boundary)
필요 시 체크포인트
[표현 스타일]

Markdown 사용
체크박스 형식 사용
실제 Cursor.AI 실습용 개발 보드처럼 작성
식별자는 Epic-001, US-001, TASK-001 형식 사용
유효한 케이스와 실패 케이스를 모두 포함
최소한 다음 작업을 포함
보드 생성
보드 유효성 검사
빈칸 탐지
후보값 필터링
완성 로직
잘못된 입력 처리
테스트 커버리지 체크포인트
[Scenario Level 정의]

L0: 기능 개요
L1: 정상 흐름
L2: 경계 상황
L3: 실패 상황
[추가 제약]

Logic 책임은 명확히 분리할 것
UI/Boundary에는 비즈니스 규칙을 넣지 말 것
Control은 검증과 해결 흐름을 조율할 것
Entity는 보드 상태를 표현할 것
모든 To-Do는 Scenario, Test, Code로 추적 가능해야 함
이제 "Magic Square 4x4 완성 시스템"의 To-Do 구조를 생성하세요.

---

**Cursor**

PRD와 보고서 경로를 확인하고 내용을 읽어 To-Do 구조를 정확히 작성합니다.



참고: 저장소에는 `docs/5.PRD_MagicSquare_4x4_TDD.md` 대신 **`docs/PRD_magic_square_4x4_tdd.md`** 가 있습니다. 아래 추적성은 해당 PRD와 `report/04_prd_journey_architecture_export_report.md`(스토리 분해), `report/02_dual_track_ui_logic_tdd_clean_architecture_report.md`(계약·`UI_*`/Dual-Track), `report/03_user_entity_ecb_tdd_implementation_report.md`·`.cursorrules`(ECB·pytest AAA)에 맞춥니다.

---

# Magic Square 4×4 완성 시스템 — 구현용 To-Do 구조

## 추적성 메타

| 구분 | 내용 |
|------|------|
| 주 소스 PRD | `docs/PRD_magic_square_4x4_tdd.md` (FR-01~05, BR-01~18, §8 Dual-Track, §9 Test Plan, §12 Traceability) |
| 스토리·여정 | `report/04_prd_journey_architecture_export_report.md` §3 |
| 계약·오류·경계 | `report/02_dual_track_ui_logic_tdd_clean_architecture_report.md` §1~2 |
| ECB·TDD 품질 | `report/03_user_entity_ecb_tdd_implementation_report.md`, `.cursorrules` |

---

## Epic-001 — 4×4 부분 비어 있는 마방진 완성(Dual-Track TDD·ECB)

**목표:** 원시 `int[][]` 입력을 경계에서 검증하고, 도메인에서 빈칸·누락 수·두 조합 시도로 `int[6]` 또는 고정 오류를 반환한다.  
**완료 조건:** PRD FR-01~05 AC 충족, NFR-01~04 만족, Concept→Code 추적 가능.

---

### User Story 목록 (Report/4 §3.3 정합)

- [ ] **US-001** — 입력 4×4·빈칸 2·값 범위·비0 중복 검증 (FR-01)  
- [ ] **US-002** — `0` 두 칸의 좌표를 row-major 순서로 산출 (FR-02)  
- [ ] **US-003** — 1~16 중 미등장 두 수를 `small`/`large`로 산출 (FR-03, 후보값 결정)  
- [ ] **US-004** — 완전 채워진 격자의 마방진(합 34) 판정 (FR-04)  
- [ ] **US-005** — 시도1→시도2 고정 순서로 완성 및 `int[6]` 반환 또는 `DOMAIN_NOT_MAGIC` (FR-05)  
- [ ] **US-006** — Boundary에서 `UI_*`·메시지·도메인 미호출·`UI_DOMAIN_FAILURE` 매핑 (PRD §8.1, Report/2 §2.2)  
- [ ] **US-007** — 도메인/경계 커버리지·결정론·입력 비변조 검증 (PRD §7 NFR)

---

## Phase A — 도메인 엔티티·값 객체 (보드 표현)

### US-001 보조 / 공통 기반

- [ ] **TASK-001** | **RED** | 도메인 보드 표현 — `Matrix4x4` 불변·복사 생성  
  - **Scenario:** L0 보드 상태 표현 / L1 유효 shape에서 생성 / L2 잘못된 shape 거부 / L3 원본 변이 방지(NFR-04)  
  - **Test:** `test_matrix4x4_construct_from_int_matrix`, `test_matrix4x4_deep_copy_immutability`  
  - **Code:** `src/.../matrix_4x4.py` (또는 설계서 논리명 `Matrix4x4`)  
  - **ECB:** Entity  
  - **체크포인트:** PRD NFR-04 — 연산은 복사본 기준, 호출자 배열 비변조 단언  

- [ ] **TASK-002** | **GREEN** | 위 RED 테스트 통과를 위한 최소 구현  
  - **Scenario:** L1  
  - **Test:** TASK-001과 동일  
  - **Code:** `Matrix4x4`  
  - **ECB:** Entity  

- [ ] **TASK-003** | **REFACTOR** | 좌표 접근·복사 헬퍼 정리(매직 넘버 4는 상수화)  
  - **Scenario:** L2  
  - **Test:** 회귀 + `test_matrix4x4_index_bounds`  
  - **Code:** `Matrix4x4`  
  - **ECB:** Entity  

- [ ] **TASK-004** | **RED** | `Position` 값 객체 — 1-index `(r,c)` ∈ [1,4]  
  - **Scenario:** L0 좌표 의미 / L1 유효 좌표 / L2 경계(1,4) / L3 잘못된 좌표  
  - **Test:** `test_position_valid_invalid`  
  - **Code:** `src/.../position.py`  
  - **ECB:** Entity(Value Object)  

- [ ] **TASK-005** | **GREEN·REFACTOR** | `Position` GREEN 후 리팩터  
  - **Scenario:** L1  
  - **Test:** TASK-004 회귀  
  - **Code:** `Position`  
  - **ECB:** Entity  

- [ ] **TASK-006** | **RED** | `MissingNumbers` — `small < large` 고정  
  - **Scenario:** L1 두 수 보관 / L3 역전 금지  
  - **Test:** `test_missing_numbers_ordering`  
  - **Code:** `src/.../missing_numbers.py`  
  - **ECB:** Entity(Value Object)  

---

## Phase B — 도메인 검증·빈칸·누락 (Logic Track)

### US-001 — 도메인 경로 검증 (FR-01 도메인 중복 검증 경로, D-RED-02~05)

- [ ] **TASK-007** | **RED** | `InputValidator`(도메인) — 크기·빈칸 수·범위·비0 중복 → `DOMAIN_*`  
  - **Scenario:** L0 입력 불변조건 / L1 각 규칙별 단일 실패 / L2 복합 위반 시 첫 실패 / L3 메시지가 아닌 코드 중심  
  - **Test:** `test_domain_validate_invalid_size` (D-RED-02), `..._blank_count` (D-RED-03), `..._out_of_range` (D-RED-04), `..._duplicate` (D-RED-05)  
  - **Code:** `src/.../input_validator.py`  
  - **ECB:** Domain Service (순수 규칙; Boundary와 코드값 분리)  
  - **체크포인트:** Report/2 INV-01~04 ↔ PRD §12 Traceability  

- [ ] **TASK-008** | **GREEN** | 도메인 검증 GREEN  
  - **Scenario:** L1  
  - **Test:** TASK-007  
  - **Code:** `InputValidator`  
  - **ECB:** Domain Service  

- [ ] **TASK-009** | **REFACTOR** | 검증 단계 분리·명명 통일 (`validateInput` 계약, Report/2 §1.4)  
  - **Scenario:** L2  
  - **Test:** 회귀  
  - **Code:** `InputValidator`  
  - **ECB:** Domain Service  

### US-002 — 빈칸 탐지 (FR-02, BR-06~07)

- [ ] **TASK-010** | **RED** | row-major로 `0` 두 칸 → `Position` 두 개 순서 고정  
  - **Scenario:** L1 PRD 데이터셋 A 기대 좌표 / L2 단일 0·세 0은 상위에서 차단 가정 / L3 빈칸 2개 아님 시 도메인 코드  
  - **Test:** `test_find_blanks_row_major_dataset_a` (TP-OK 계열), `test_find_blanks_invalid_count_domain`  
  - **Code:** `blank_finder.py` 또는 `Matrix4x4` 확장(설계서 `BlankFinder`)  
  - **ECB:** Domain Service (+ Entity 읽기)  

- [ ] **TASK-011** | **GREEN·REFACTOR** | 빈칸 탐지 GREEN·리팩터  
  - **Scenario:** L1~L2  
  - **Test:** TASK-010  
  - **Code:** `BlankFinder`  
  - **ECB:** Domain Service  

### US-003 — 후보값(누락 두 수) 산출 (FR-03, BR-08)

- [ ] **TASK-012** | **RED** | `findMissingNumbers` — 미등장이 정확히 2개가 아니면 `DOMAIN_INVALID_MISSING_COUNT` (D-RED-06)  
  - **Scenario:** L1 정상 시 small/large / L3 누락 개수 불일치  
  - **Test:** `test_missing_numbers_two_values`, `test_missing_numbers_invalid_count`  
  - **Code:** `missing_number_finder.py` (`MissingNumbers` 반환)  
  - **ECB:** Domain Service  

- [ ] **TASK-013** | **GREEN·REFACTOR** | 누락 탐색 GREEN·리팩터  
  - **Scenario:** L1  
  - **Test:** TASK-012  
  - **Code:** `MissingNumberFinder`  
  - **ECB:** Domain Service  

---

## Phase C — 판정·완성 로직 (Logic Track)

### US-004 — 마방진 판정 (FR-04)

- [ ] **TASK-014** | **RED** | `MagicSquareJudge` — 완전·1~16 채워진 행렬만 `true/false` (FR-04-AC)  
  - **Scenario:** L1 알려진 마방진 true / L2 한 줄만 틀리면 false / L3 판정 결정론  
  - **Test:** `test_judge_known_magic_true`, `test_judge_one_line_wrong_false`, `test_judge_idempotent`  
  - **Code:** `magic_square_judge.py`  
  - **ECB:** Domain Service  

- [ ] **TASK-015** | **GREEN·REFACTOR** | 판정 GREEN·행·열·대각 분리 가독성  
  - **Scenario:** L1~L2  
  - **Test:** TASK-014  
  - **Code:** `MagicSquareJudge`  
  - **ECB:** Domain Service  

### US-005 — 두 조합 시도·`int[6]` (FR-05, BR-13~18)

- [ ] **TASK-016** | **RED** | `FillStrategy`/`TwoBlankSolver` — 시도1만 성공·시도2만 성공·둘 다 실패 (D-RED-07, D-RED-08, TP-OK-01/02, TP-FAIL-01)  
  - **Scenario:** L0 완성 흐름 / L1 TP-OK-01·02 / L2 시도1 성공 시 시도2 미호출(FR-05-AC-03) / L3 DOMAIN_NOT_MAGIC  
  - **Test:** `test_solve_attempt1_success`, `test_solve_attempt2_only_success`, `test_solve_both_fail_domain_not_magic`  
  - **Code:** `two_blank_solver.py` 또는 `fill_strategy.py`  
  - **ECB:** Domain Service (+ 내부에서 `Judge` 사용; Boundary 의존 없음)  
  - **체크포인트:** 채움은 **행렬 복사본**에 적용 후 판정(NFR-04)  

- [ ] **TASK-017** | **GREEN** | 솔버 GREEN  
  - **Scenario:** L1  
  - **Test:** TASK-016  
  - **Code:** `TwoBlankSolver`  
  - **ECB:** Domain Service  

- [ ] **TASK-018** | **REFACTOR** | 출력 `[r1,c1,n1,r2,c2,n2]` 조립 전용 함수 분리·명명  
  - **Scenario:** L2  
  - **Test:** 회귀 + `test_output_schema_length_six`  
  - **Code:** `TwoBlankSolver`  
  - **ECB:** Domain Service  

---

## Phase D — Control (유스케이스 조율)

- [ ] **TASK-019** | **RED** | `MagicSquareCompletionControl`(가칭) — 검증→빈칸→누락→솔브 순서, 도메인 실패 전파  
  - **Scenario:** L1 단일 진입점 성공 / L3 도메인 오류 코드 전달  
  - **Test:** `test_control_happy_path`, `test_control_propagates_domain_error`  
  - **Code:** `src/.../magic_square_completion_control.py`  
  - **ECB:** Control — **비즈니스 규칙은 위임만**, 조립·순서만  

- [ ] **TASK-020** | **GREEN·REFACTOR** | Control GREEN·의존성 주입 형태 정리  
  - **Scenario:** L1  
  - **Test:** TASK-019  
  - **Code:** `MagicSquareCompletionControl`  
  - **ECB:** Control  

---

## Phase E — Boundary (UI Track): 잘못된 입력 처리·계약

### US-006 — 경계 검증·매핑 (FR-01 경계, FR-05 실패 매핑, Report/2 §2.2)

- [ ] **TASK-021** | **RED** | Boundary 입력 검증 — `UI_INVALID_SIZE`, `UI_INVALID_BLANK_COUNT`, `UI_OUT_OF_RANGE`, `UI_DUPLICATE_NONZERO` 및 **고정 메시지** (UI-RED-01~04)  
  - **Scenario:** L0 원시 입력 거부 / L1 각 코드별 한 케이스 / L2 도메인 미호출(FR-01-AC-05) / L3 메시지 문자열 완전 일치  
  - **Test:** `test_boundary_ui_invalid_size`, `test_boundary_ui_blank_count`, `test_boundary_ui_out_of_range`, `test_boundary_ui_duplicate`, `test_boundary_domain_never_called_on_ui_failure`  
  - **Code:** `magic_square_boundary.py` 또는 `boundary/magic_square_input.py`  
  - **ECB:** Boundary — **비즈니스 규칙 넣지 않음**(형·개수·범위·중복만)  

- [ ] **TASK-022** | **GREEN** | Boundary GREEN  
  - **Scenario:** L1  
  - **Test:** TASK-021  
  - **Code:** Boundary 모듈  
  - **ECB:** Boundary  

- [ ] **TASK-023** | **RED** | 성공 시 `result: int[6]`, 도메인 `DOMAIN_NOT_MAGIC` → `UI_DOMAIN_FAILURE` + `no valid magic-square completion found` (UI-RED-05~06, DEC-01)  
  - **Scenario:** L1 성공 스키마 / L3 도메인 실패 매핑  
  - **Test:** `test_boundary_success_schema`, `test_boundary_domain_failure_mapping`  
  - **Code:** Boundary 응답 DTO/딕셔너리 빌더  
  - **ECB:** Boundary  

- [ ] **TASK-024** | **GREEN·REFACTOR** | 성공·실패 응답 조립 리팩터  
  - **Scenario:** L2  
  - **Test:** 회귀  
  - **Code:** Boundary  
  - **ECB:** Boundary  

---

## Phase F — 통합·회귀·품질 (Report/3·NFR)

### US-007 — 테스트 커버리지·비기능

- [ ] **TASK-025** | **RED** | 통합 시나리오 — PRD §9.1 TP-OK-01/02, TP-FAIL-01~05, §9.3 데이터셋 A  
  - **Scenario:** L1 엔드투엔드 / L3 실패 시 성공 필드 미노출(PROP-04)  
  - **Test:** `test_integration_tp_ok_01`, `test_integration_tp_ok_02`, `test_integration_tp_fail_*`, `test_integration_dataset_a`  
  - **Code:** `tests/integration/test_magic_square_flow.py` + Facade(선택)  
  - **ECB:** Integration (Boundary→Control→Entity 경로)  

- [ ] **TASK-026** | **GREEN** | 통합 GREEN  
  - **Scenario:** L1  
  - **Test:** TASK-025  
  - **Code:** 진입점 조립  
  - **ECB:** —  

- [ ] **TASK-027** | **REFACTOR** | 공통 fixture·데이터셋 A/B 공유  
  - **Scenario:** L2  
  - **Test:** 동일  
  - **Code:** `tests/conftest.py`  
  - **ECB:** —  

- [ ] **TASK-028** | **체크포인트(전용)** | 커버리지 게이트 — **도메인 ≥95%, 경계 ≥85%** (PRD NFR-01~02)  
  - **Scenario:** L0 품질 게이트  
  - **Test:** `pytest --cov=...` 리포트; CI 또는 로컬 스크립트  
  - **Code:** `pyproject.toml` / `pytest.ini` / CI 설정  
  - **ECB:** —  
  - **체크포인트:** 미달 시 RED 유지, 리팩터로 분기·데드 코드 제거  

- [ ] **TASK-029** | **체크포인트** | 결정론·입력 비변조 회귀 (NFR-03~04)  
  - **Scenario:** L2  
  - **Test:** `test_same_input_same_output`, `test_input_matrix_unchanged_after_solve`  
  - **Code:** 통합 + `Matrix4x4`/Solver  
  - **ECB:** Entity + Integration  

- [ ] **TASK-030** | **REFACTOR** | ECB 디렉터리 정리, `.cursorrules`·Report/3과 동일한 pytest AAA·타입힌트 점검  
  - **Scenario:** L0 코드베이스 일관성  
  - **Test:** 전체 스위트  
  - **Code:** 패키지 구조 `boundary` / `control` / `entity` / `domain`  
  - **ECB:** 아키텍처 전반  

---

## Dual-Track·RED/GREEN/REFACTOR 운영 요약

| 트랙 | 권장 병렬 작업 | 금지(PRD §8.3) |
|------|----------------|----------------|
| **UI(Boundary)** | TASK-021~024와 도메인 TASK-007~018 병렬 가능 | 경계 실패 시 도메인이 이미 호출되는 구조로 나중에 땜질 |
| **Logic(Domain)** | 엔티티→검증→빈칸→누락→판정→솔버 순 | Boundary 문자열/코드에 도메인이 의존 |

---

## Concept-to-Code 추적 (예시 한 줄)

| Concept | PRD | Test | Code |
|---------|-----|------|------|
| 빈칸 2·row-major | FR-02, BR-06~07 | `test_find_blanks_row_major_dataset_a` | `BlankFinder` |
| 후보 두 수 | FR-03, BR-08 | `test_missing_numbers_two_values` | `MissingNumberFinder` |
| 잘못된 입력(UI) | FR-01 | `test_boundary_ui_*` | Boundary |
| 완성 실패 | FR-05 | `test_solve_both_fail_*`, `test_boundary_domain_failure_mapping` | Solver + Boundary 매핑 |

---

이 구조로 Cursor 보드에 붙이려면 **Epic → User Story → Phase 순으로 TASK 체크박스**만 옮기면 됩니다. 파일명(`src/...`)은 레포 실제 패키지명에 맞춰 바꾸면 됩니다.

---

**User**

Ｔｏ－Ｄｏ　리스트를 포함해 READMD.md 파일을 만들고 싶습니다. 무슨 문서를 참조하면 좋을까요?




---

**Cursor**

`README.md`에 **프로젝트 소개 + 실행 방법 + To-Do**를 넣을 때는 아래를 참조하면 됩니다. (파일명은 보통 **`README.md`** 입니다.)

## README 본문·비전에 쓸 문서

1. **`docs/PRD_magic_square_4x4_tdd.md`**  
   - 한 줄 요약, 범위(In/Out), 핵심 계약(4×4, `0` 2개, `int[6]`, Magic 34), Dual-Track TDD 한 줄.  
   - **To-Do 항목·완료 조건**의 **주 근거**로 가장 적합합니다.

2. **`docs/DESIGN_layered_architecture_tdd_magic_square_4x4.md`** (있다면)  
   - 레이어(Boundary / Domain), ECB에 가까운 구성 요약용.

3. **`report/04_prd_journey_architecture_export_report.md`**  
   - Epic / Journey / User Story 수준의 **한 장짜리 맥락**을 README에 넣을 때.

## 개발 방식·규칙·추적성에 쓸 문서

4. **`report/02_dual_track_ui_logic_tdd_clean_architecture_report.md`**  
   - `UI_*` 코드·메시지, 경계 vs 도메인, Dual-Track 설명 한 단락.

5. **`report/03_user_entity_ecb_tdd_implementation_report.md`** + **`.cursorrules`**  
   - ECB, pytest AAA, `boundary → control → entity`를 README의 “기여/코딩 규칙”에 쓸 때.

6. **`report/01_problem_definition_report.md`**  
   - 문제 정의·Invariant 강조가 필요할 때만 (선택).

## To-Do 리스트 specifically

- **할 일·완료 기준**은 PRD의 **FR-01~05 / AC**를 기준으로 두는 것이 좋고,  
- README가 너무 길어지면 **To-Do는 별도 파일**(예: `docs/TODO_magic_square_4x4.md`)에 두고 README에서는 **한두 문장 + 링크**만 두는 방식이 읽기 좋습니다.

정리하면, **README = PRD(필수) + (선택) DESIGN·04번 보고서 + (선택) 02·03·.cursorrules**, **To-Do = PRD FR 기반**이면 문서끼리 엇갈리지 않습니다.

---

**User**

@c:\DEV\MagicSquare\ 에 있는 README 본문·To-Do·검증 기준은 docs/5.PRD_MagicSquare_4x4_TDD.md를 중심에 두고, 스토리 표현은 Report/4, 오류·계약 요약은 Report/2, 실행·ECB·TDD는 Report/3 + pyproject.toml + Cursor 규칙, 문서 관계 한 줄은 Report/5를 참조해서 To-Do 리스트를 포함한 MagicSquare를 만들기 위한 README.md 파일을 만들어줘.

---

**Cursor**

프로젝트의 실제 파일 경로와 `pyproject.toml`, Report/5 존재 여부를 확인합니다.



`pyproject.toml`이 저장소에 없어 `.cursorrules`의 Python/pytest·커버리지 기준을 반영하고, `report/05`는 없으므로 `report/04` §4~6의 문서 관계·후속 권장 문구에 맞춥니다. PRD 실제 경로는 `docs/PRD_magic_square_4x4_tdd.md`입니다.



T-FR-05 줄의 백틱 오타를 수정합니다.



`c:\DEV\MagicSquare\README.md`를 추가해 두었습니다. 요지만 정리합니다.

## 반영한 내용

- **중심 문서:** `docs/PRD_magic_square_4x4_tdd.md` — 본문·To-Do·검증(NFR) 모두 PRD를 기준으로 두었고, 질문에 나온 `docs/5.PRD_...`는 **현재 repo에는 없음**을 박스로 안내하고 실제 PRD 경로로 연결했습니다.
- **Report/4:** §3에 맞춰 User Story 요약, 에픽·Track 체크리스트에 반영.
- **Report/2:** `UI_*` ↔ 고정 `message` 표.
- **Report/3 + Cursor:** ECB 의존 방향, pytest·AAA, RED/GREEN/REFACTOR, Python 3.10+.
- **`pyproject.toml`:** 루트에 **아직 없을 수 있음**을 적고, 생기면 그걸 실행 기준으로 쓰라고 했습니다. (현재 `glob` 기준으로도 파일 없음.)
- **Report/5:** repo에 `report/05`는 없으므로, [report/04](report/04_prd_journey_architecture_export_report.md) **§4~6·§6 권장**이 말하는 “PRD+DESIGN이 SSoT, 04가 인덱스·내보내기” 문장을 **문서 관계 한 줄**로 쓰고, 향후 `05` 분리 시에 대비한다고 명시했습니다.
- **To-Do:** Epic-001(E1-Track-A/B, Entity, Control, 품질) + T-FR-01~05·잘못된 입력·커버리지 체크박스.

백틱이 깨져 있던 `T-FR-05` 한 줄은 `int[6]`, 실패 시 코드로 문장을 고쳐 두었습니다.

---

**User**

Report 폴더에 작업한 내용을 보고서로 내보내줘

---

**Cursor**

기존 보고서 형식과 최근 산출물을 확인한 뒤 `report` 폴더에 내보내기 보고서를 작성합니다.



기존 보고서(특히 `04`) 형식에 맞춰 `README` 작성·문서 체계 정리 작업을 내보내는 `report/05` 보고서를 작성합니다.



README의 ‘report/05 없음’ 문구를 새 보고서와 맞게 수정합니다.



작업 반영했습니다.

## 생성한 보고서

**`report/05_readme_project_export_report.md`**

- **§1** 작업 목적: `README.md`·문서 맵·To-Do·온보딩
- **§2** 산출물: `README.md` + 본 보고서, `report/01`~`04`와의 역할 구분 표
- **§3** README 섹션별 요약과 근거(PRD / Report/2·3·4)
- **§4** 본 문서 작업용 검증 기준(VE-01~04)
- **§5** 후속 권장(`pyproject.toml`, TODO 분리 등)
- **§6** 참조 경로 목록

형식은 **`report/04_prd_journey_architecture_export_report.md`**와 같이 표·절 번호 위주로 맞춰 두었습니다.

## README 정리

`README.md`의 **문서·근거 표**에 Report/5 행을 넣었고, **문서 관계 한 줄**과 **참고 링크**를 새 보고서와 연결해 두었습니다.

이제 **문서 인덱스**는 `report/04`, **README 작성·내보내기**는 **`report/05`**에서 따라가면 됩니다.

