# Magic Square (4×4) — TDD·ECB 연습

부분적으로 비어 있는 4×4 격자(빈 칸 `0` 정확히 2개)에서, 누락된 두 숫자를 **고정된 시도 순서**로 배치해 마방진(합 34)을 완성하거나, 유효하지 않은 입력·해가 없는 경우 **고정 코드·메시지**로 실패를 반환하는 **로컬·순수 도메인** 시스템을 목표로 합니다. 알고리즘 경쟁이 아니라 **Invariant·계약·Dual-Track TDD·리팩터링**을 연습하는 것이 핵심입니다.

> **주 요구·검증 기준(SSoT):** `docs/PRD_magic_square_4x4_tdd.md`  
> (다른 문서·대화에서 `docs/5.PRD_MagicSquare_4x4_TDD.md`로 부르는 경우, 본 repo에서는 위 경로의 PRD가 해당 역할을 합니다.)

---

## 현재까지의 작업 (저장소 스냅샷)

| 구분 | 상태 |
|------|------|
| **요구·설계 문서** | **PRD v2.1** 고정: Dual-Track을 **UX Contract / Logic Rule** 언어로 정리(§2.3), **CI·커버리지 게이트**·산출물(§7.1, **NFR-06**), Track A/B 정의(§8.0), 경계·도메인 테스트 역할(§8.4), **§9.1** 시나리오 매핑 표 등. 계층 설계는 `docs/DESIGN_layered_architecture_tdd_magic_square_4x4.md`. 문제 정의·Dual-Track·ECB 예시·여정 인덱스·README 내보내기·PRD 갱신 이력·테스트 케이스 명세 내보내기는 `report/01`~`07` 참조. |
| **구현 코드** | PRD **FR-01~05**(경계 검증·마방진 도메인 솔버)는 **아직 없음**. ECB·pytest AAA 패턴 예시로 **`User` 엔티티**와 해당 테스트만 존재(`src/entity/models/user.py`, `tests/entity/` — [report/03](report/03_user_entity_ecb_tdd_implementation_report.md)과 같은 취지). |
| **빌드 설정** | 루트 **`pyproject.toml`** — 편집 가능 설치 `pip install -e ".[dev]"`, `pytest`·(선택) `pytest-cov`·`[cov]` extra. |

---

## 문서·근거 (무엇을 보면 되나)

| 역할 | 문서 | 비고 |
|------|------|------|
| 본문·To-Do·검증 기준의 중심 | [docs/PRD_magic_square_4x4_tdd.md](docs/PRD_magic_square_4x4_tdd.md) | v2.1 — §2.3·§7.1·§9.1 등; FR-01~05, BR, NFR, Dual-Track, Traceability |
| 레이어·계약·TC ID (설계) | [docs/DESIGN_layered_architecture_tdd_magic_square_4x4.md](docs/DESIGN_layered_architecture_tdd_magic_square_4x4.md) | IC/OC, Domain/Boundary 구조 |
| 문제 인식·Invariant | [report/01_problem_definition_report.md](report/01_problem_definition_report.md) | 초기 문제 정의 |
| 스토리·에픽·여정 표현 | [report/04_prd_journey_architecture_export_report.md](report/04_prd_journey_architecture_export_report.md) | §3: Epic, Journey, User Stories, 기술 시나리오 요약 |
| README·온보딩 작업 내보내기 | [report/05_readme_project_export_report.md](report/05_readme_project_export_report.md) | `README.md` 작성 배경·산출물·검증·후속 권장 |
| PRD v2.1 갱신·Dual-Track/MLOps 정렬 이력 | [report/06_dual_track_mlops_prd_update_report.md](report/06_dual_track_mlops_prd_update_report.md) | 변경 요약·§2.3·§7.1·§9.1·DEC-05 등 |
| 테스트 케이스 명세 내보내기 | [report/07_test_case_specification_export_report.md](report/07_test_case_specification_export_report.md) | TC-MS-A~D·`docs/test_case_specification_magic_square_4x4.md` 인덱스 |
| 경계 `UI_*`·메시지·Dual-Track 요약 | [report/02_dual_track_ui_logic_tdd_clean_architecture_report.md](report/02_dual_track_ui_logic_tdd_clean_architecture_report.md) | §2.2 테이블, `UI-RED-*`, §0 PRD 정합 |
| 실행·ECB·엔티티 TDD 절차 예시 | [report/03_user_entity_ecb_tdd_implementation_report.md](report/03_user_entity_ecb_tdd_implementation_report.md) | ECB·pytest AAA·`entity` 샘플 |
| 에디터/에이전트 규칙 | [.cursorrules](.cursorrules) | ECB 방향, RED/GREEN/REFACTOR, pytest, coverage 최소값 |
| 빌드·의존성 | `pyproject.toml` (프로젝트 루트) | Python 3.10+·`dev`·`cov` optional-dependencies. |

**문서 관계(한 줄):** 요구사항의 **단일 진실 공급원**은 PRD와 DESIGN으로 두고, PRD·여정·설계 인덱스는 [report/04](report/04_prd_journey_architecture_export_report.md) §4~6에 정리한다. 프로젝트 진입 문서(`README.md`) 작성·문서 맵 내보내기는 [report/05](report/05_readme_project_export_report.md)에서 보고한다. PRD v2.1 개정 요약은 [report/06](report/06_dual_track_mlops_prd_update_report.md)을 본다. **소프트웨어 테스트 케이스 명세** 산출·배경은 [report/07](report/07_test_case_specification_export_report.md)과 `docs/test_case_specification_magic_square_4x4.md`를 본다. `docs/5_*` 등 별도 분리는 report/04 §6 권장과 같은 취지로 유지할 수 있다.

---

## 도메인 요약 (PRD와 동일)

- 격자: **4×4**, 값은 **`0` 또는 1~16** — `0`은 빈 칸, **정확히 2곳**  
- 0을 제외한 **중복 없음**  
- 완성 시 **모든 행·열·두 대각선의 합 = 34**  
- 성공 출력: `int[6]` = `[r1,c1,n1,r2,c2,n2]`, 좌표 **1-index**  
- 해는 **누락 두 수**를 `small`/`large`로 두고, `small`→첫 빈칸·`large`→둘째 빈칸 시도 후, 실패 시 **역배치**한 뒤 처음 맞는 배치를 반환(자세한 규칙·실패는 PRD §5~6).  

**경계는 비즈니스 판정을 하지 않는다:** 입력 형·빈칸 수·범위·중복만 검증(FR-01), 도메인은 논리 솔버·불변조건(FR-02~05).

---

## 경계 `UI_*`·고정 메시지 (Report/2 요약, PRD §8.1과 합치)

| 코드 | `message` (고정) |
|------|------------------|
| `UI_INVALID_SIZE` | `matrix must be 4x4` |
| `UI_INVALID_BLANK_COUNT` | `matrix must contain exactly two zeros` |
| `UI_OUT_OF_RANGE` | `values must be 0 or in [1,16]` |
| `UI_DUPLICATE_NONZERO` | `non-zero values must be unique` |
| `UI_DOMAIN_FAILURE` | `no valid magic-square completion found` |

도메인 측 코드·매핑·테스트 ID는 PRD `§8.2`·`§12` 및 DESIGN을 따른다.

---

## User Story (Report/4 §3.3 — 표현은 여기서 가져옴)

- 입력 **4×4**·빈 칸 2·범위·**비0 중복** 검증  
- **`0` 두 칸** 좌표를 **row-major**로  
- **1~16 중 미등장 2개**를 `small`/`large`  
- **행·열·대각 합 34** 판정  
- **시도1→시도2** 고정 순서로 `int[6]`, 1-index 반환  

---

## 검증 기준 (PRD §7, README 요약)

| ID | 기준 (요지) | 확인 |
|----|-------------|------|
| NFR-01 | **도메인** 라인/브랜치 커버리지 **≥ 95%** | 커버리지 리포트 |
| NFR-02 | **경계(Boundary)** 커버리지 **≥ 85%** | 동일 |
| NFR-03 | 동일 입력 → 동일 성공 배열 또는 동일 오류 코드·메시지 | 반복 테스트 |
| NFR-04 | 호출자 `int[][]` **비변조**(내부는 복사본으로 연산) | 전후 스냅샷/단언 |
| NFR-05 | 성능(선택): 단일 요청 **50ms** 이내 등 | 벤치마크(선택) |
| NFR-06 | **CI**: NFR-01·02 미달 시 **파이프 실패**(§7.1 권장 단계·아티팩트) | CI 로그·커버리지 리포트 |

> `.cursorrules`는 저장소 전역 `coverage_minimum: 80%`를 명시 — **마방진 도메인/경계에 대해서는 PRD NFR(95/85)을 우선**한다.

---

## 구현·실행 (ECB + TDD, Report/3 + Cursor 규칙)

- **의존 방향:** `boundary → control → entity` (entity는 상위 미의존).  
- **TDD:** RED → GREEN → REFACTOR(`.cursorrules` `tdd_rules`).  
- **테스트:** `pytest`, **AAA**, 테스트 함수·파일 `test_` 접두, 타입힌트·공개 API Google docstring(Report/3·`.cursorrules`과 동일).  
- **Python:** 3.10+ (`.cursorrules` `code_style`).  

**한 번만 (가상환경·개발 의존성):**

```powershell
cd c:\DEV\MagicSquare
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
pip install -e ".[dev]"
```

**테스트 (전체):** 루트에서 `pytest` — `pyproject.toml`의 `testpaths`·`pythonpath=src`로 `entity`·`magic_square`를 import한다. `tests/domain`의 TC-MS RED 스켈레톤은 아직 `pytest.fail("RED")`라 **실패가 정상**이고, 엔티티 샘플만 보려면 `pytest tests/entity -q`.

**커버리지:** `pip install pytest-cov` 또는 `pip install -e ".[cov]"` 후, 배포 이름은 `magicsquare`이지만 측정 대상 **임포트 패키지**는 `magic_square`·`entity`이다.

```powershell
pytest --cov=magic_square --cov=entity --cov-report=term-missing
pytest --cov=magic_square --cov=entity --cov-report=html
# htmlcov/index.html
```

---

## To-Do (PRD FR·Dual-Track·C2C 추적)

**주 소스:** [PRD](docs/PRD_magic_square_4x4_tdd.md) FR-01~05, BR, §9 Test Plan, §12 Traceability. **설계 순서:** [DESIGN](docs/DESIGN_layered_architecture_tdd_magic_square_4x4.md).

**추적성(Concept-to-Code):** 각 작업은 **Task → FR(요구)·PRD TC ID(해당 시) → Scenario 수준 → 테스트 이름**으로 내려갈 수 있게 유지한다. PRD §9.1·§12의 `UI-RED-*`, `D-RED-*`, `TP-OK`/`TP-FAIL`과 연결한다.

**범위 주의:** 빈 칸 두 개·누락 두 수는 **결정론적 규칙(FR-02~03)** 이므로 일반 탐색 알고리즘(N-Queen 등)은 **본 PRD 범위에 없음**. 성능은 NFR-05(선택, 예: 50ms)로 별도 검증한다.

**별도 연습(마방진 Epic과 무관):** [report/03](report/03_user_entity_ecb_tdd_implementation_report.md) 패턴의 **`User` 엔티티·`tests/entity`** 는 ECB 샘플이며, 아래 Epic 체크와는 분리한다.

### Scenario 수준 (테스트·슬라이드 정합)

| 수준 | 의미 |
|------|------|
| **L0** | 기능 개요·스코프 |
| **L1** | 정상 흐름(해피 패스) |
| **L2** | 경계·에지(합·좌표 경계 등) |
| **L3** | 실패·오류 경로(`UI_*`, `DOMAIN_*`, 무해) |

---

### Epic-001 — 4×4 마방진 완성 시스템 (Dual-Track TDD, ECB)

#### Phase 0 — Entity / VO (선행, NFR-04·FR 출력 정합)

- **US-E01 — 보드·좌표·누락 값 객체**

  - [ ] **TASK-E01** 4×4 보드 표현(불변·깊은 복사·원본 `int[][]` 비변조) — **NFR-04**, DESIGN  
    - [ ] RED: 유효 행렬에서 생성·호출 후 원본 동등  
    - [ ] GREEN: 최소 구현  
    - [ ] REFACTOR: 인덱스·상수(`SIZE=4`) 정리  

  - [ ] **TASK-E02** `Position` 또는 동등 VO — 좌표 **1-index**, 범위 1~4 — **FR-02·FR-05** 출력  
    - [ ] RED / GREEN / REFACTOR  

  - [ ] **TASK-E03** `MissingNumbers`(또는 동등) — `small` ≤ `large` 고정 — **FR-03**  

---

#### Track B — Domain (Logic Rule, FR-02~05)

- **US-D01 — 빈칸(row-major)** — **FR-02**  

  - [ ] **TASK-D01** 두 개의 `0` 위치를 row-major 순으로 `(r1,c1),(r2,c2)` — FR-02-AC-02  
    - [ ] RED: PRD §9 데이터셋·예상 좌표 대조  
    - [ ] GREEN / REFACTOR  

- **US-D02 — 누락 두 수** — **FR-03**  

  - [ ] **TASK-D02** 1~16 중 미등장 두 수 → `small`, `large`; 개수 불일치 시 `DOMAIN_INVALID_MISSING_COUNT` — FR-03-AC-01  
    - [ ] RED / GREEN / REFACTOR  

- **US-D03 — 마방진 판정(합 34)** — **FR-04**  

  - [ ] **TASK-D03** 완전 채워진 4×4에 대해 행·열·두 대각 합 34 여부 — FR-04-AC-01~02  
    - [ ] RED: 알려진 마방진 true·일부 깨진 행 false  
    - [ ] GREEN / REFACTOR  

- **US-D04 — 두 조합 시도·해 반환** — **FR-05**  

  - [ ] **TASK-D04** 시도1(`small`→첫 빈칸, `large`→둘째) 후 FR-04; 성공 시 **시도2 생략**(FR-05-AC-03). 실패 시 시도2(역배치). 둘 다 실패 시 `DOMAIN_NOT_MAGIC`. 성공 시 `int[6]` — FR-05-AC-01~06  
    - [ ] RED: TP-OK·TP-FAIL·D-RED 시나리오별 실패 테스트 먼저  
    - [ ] GREEN  
    - [ ] REFACTOR: 채움은 **복사본**에 적용 후 판정(NFR-04)  

- **US-D05 — (선택) 도메인 재검증 경로** — PRD §8.4 / DESIGN과 택1 정책 일치  

  - [ ] **TASK-D05** Boundary 통과 행렬에 대한 도메인 단위 테스트와 솔버 내부 재검증 (a)/(b) 중 **한 가지만** 선택해 IT와 모순 없게 유지  

---

#### Track A — Boundary (UX Contract, FR-01 + 실패 매핑)

- **US-B01 — 원시 입력 검증** — **FR-01**  

  - [ ] **TASK-B01** 4×4 아님·빈칸 수≠2·0/1~16 밖·비0 중복 → 각각 `UI_*`·**고정 `message`** (본 README 표와 문자열 일치)  
    - [ ] RED: `UI-RED-01`~`04` 대응 실패 케이스  
    - [ ] GREEN  
    - [ ] REFACTOR: 검증 순서·조기 종료 명확화  

  - [ ] **TASK-B02** 위 실패 시 **도메인 `solve`/솔버 호출 0회** — **FR-01-AC-05** (스파이/모킹)  

- **US-B02 — 도메인 실패를 경계 응답으로**  

  - [ ] **TASK-B03** `DOMAIN_NOT_MAGIC` → `UI_DOMAIN_FAILURE` + `no valid magic-square completion found` — FR-05·§8.1  
    - [ ] RED / GREEN / REFACTOR  

---

#### Phase C — Control

- **US-C01 — 유스케이스 조율**  

  - [ ] **TASK-C01** Boundary 통과 시에만: 검증(필요 시)·빈칸→누락→솔버 호출·결과 조립 — **규칙은 Entity/Domain에만**, Control은 순서·위임  

---

#### Phase I — 통합·품질·회귀

- **US-I01 — 끝단·시나리오**  

  - [ ] **TASK-I01** PRD §9.1 매핑표·TP-OK/TP-FAIL·잘못된 입력 시나리오 통합 테스트  

- **US-I02 — 비기능·CI**  

  - [ ] **TASK-I02** NFR-03 결정론·NFR-04 비변조 회귀 테스트  
  - [ ] **TASK-I03** 커버리지: Domain **≥95%**, Boundary **≥85%** (NFR-01·02); CI에서 미달 시 실패(NFR-06, §7.1)  
  - [ ] **TASK-I04** 회귀 시 기존 TC ID·테스트 삭제 금지(§9.3 정책) — 리팩터는 Green 유지 후  

- **US-I03 — 리팩터 게이트**  

  - [ ] **TASK-I05** Track A·B 테스트가 모두 Green일 때만 ECB 디렉터리·명명 정리(`.cursorrules` refactor_phase)  

---

### 추적 매트릭스 (구현 진행 시 채움)

PRD §12·pytest 노드 이름과 맞추어 행을 추가한다.

| Task ID | FR / TC (예) | Scenario | 테스트 이름(가칭) | 상태 |
|---------|----------------|----------|-------------------|------|
| TASK-B01 | FR-01, UI-RED-01~04 | L3 | `test_boundary_ui_invalid_size` 등 | ⬜ TODO |
| TASK-B02 | FR-01-AC-05 | L3 | `test_domain_never_called_on_boundary_fail` | ⬜ TODO |
| TASK-D03 | FR-04, TP-OK-* | L1 | `test_judge_known_magic_square` | ⬜ TODO |
| TASK-D04 | FR-05 | L1/L3 | `test_solve_attempt_order`, `test_domain_not_magic` | ⬜ TODO |
| TASK-I03 | NFR-01·02 | L0 | `pytest --cov` 리포트 | ⬜ TODO |

---

### 한 줄 요약 (기존 FR 체크리스트)

| FR | 내용 |
|----|------|
| FR-01 | 경계: 형·빈칸·범위·중복 → `UI_*`, 솔버 미호출 |
| FR-02 | 빈칸 두 곳, row-major, 1-index |
| FR-03 | 누락 두 수 `small`/`large` |
| FR-04 | 완전 격자 마방진 판정(34) |
| FR-05 | 두 조합 시도, `int[6]` 또는 `DOMAIN_NOT_MAGIC` / `UI_DOMAIN_FAILURE` |

---

## 라이선스

(미정이면 팀/저자 정책에 맞게 이 줄을 바꾼다.)

---

## 참고 링크 (한 번에)

- [PRD (중심)](docs/PRD_magic_square_4x4_tdd.md)  
- [DESIGN](docs/DESIGN_layered_architecture_tdd_magic_square_4x4.md)  
- [Report/1 — 문제 정의](report/01_problem_definition_report.md)  
- [Report/4 — 스토리·에픽·인덱스](report/04_prd_journey_architecture_export_report.md)  
- [Report/5 — README·온보딩 내보내기](report/05_readme_project_export_report.md)  
- [Report/6 — PRD v2.1·Dual-Track/MLOps 갱신](report/06_dual_track_mlops_prd_update_report.md)  
- [Report/7 — 테스트 케이스 명세 내보내기](report/07_test_case_specification_export_report.md)  
- [Report/2 — 경계·계약](report/02_dual_track_ui_logic_tdd_clean_architecture_report.md)  
- [Report/3 — ECB·TDD 예시](report/03_user_entity_ecb_tdd_implementation_report.md)  
- [`.cursorrules`](.cursorrules)  
