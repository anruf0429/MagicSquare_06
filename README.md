# Magic Square (4×4) — TDD·ECB 연습

부분적으로 비어 있는 4×4 격자(빈 칸 `0` 정확히 2개)에서, 누락된 두 숫자를 **고정된 시도 순서**로 배치해 마방진(합 34)을 완성하거나, 유효하지 않은 입력·해가 없는 경우 **고정 코드·메시지**로 실패를 반환하는 **로컬·순수 도메인** 시스템을 목표로 합니다. 알고리즘 경쟁이 아니라 **Invariant·계약·Dual-Track TDD·리팩터링**을 연습하는 것이 핵심입니다.

> **주 요구·검증 기준(SSoT):** `docs/PRD_magic_square_4x4_tdd.md`  
> (다른 문서·대화에서 `docs/5.PRD_MagicSquare_4x4_TDD.md`로 부르는 경우, 본 repo에서는 위 경로의 PRD가 해당 역할을 합니다.)

---

## 현재까지의 작업 (저장소 스냅샷)

| 구분 | 상태 |
|------|------|
| **요구·설계 문서** | **PRD v2.1** 고정: Dual-Track을 **UX Contract / Logic Rule** 언어로 정리(§2.3), **CI·커버리지 게이트**·산출물(§7.1, **NFR-06**), Track A/B 정의(§8.0), 경계·도메인 테스트 역할(§8.4), **§9.1** 시나리오 매핑 표 등. 계층 설계는 `docs/DESIGN_layered_architecture_tdd_magic_square_4x4.md`. 문제 정의·Dual-Track·ECB 예시·여정 인덱스·README 내보내기·PRD 갱신 이력은 `report/01`~`06` 참조. |
| **구현 코드** | PRD **FR-01~05**(경계 검증·마방진 도메인 솔버)는 **아직 없음**. ECB·pytest AAA 패턴 예시로 **`User` 엔티티**와 해당 테스트만 존재(`src/entity/models/user.py`, `tests/entity/` — [report/03](report/03_user_entity_ecb_tdd_implementation_report.md)과 같은 취지). |
| **빌드 설정** | 루트에 **`pyproject.toml` 없음**. 추가 시 Python 버전·pytest·커버리지의 단일 기준으로 삼을 것([report/05](report/05_readme_project_export_report.md) 후속 권장과 동일). |

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
| 경계 `UI_*`·메시지·Dual-Track 요약 | [report/02_dual_track_ui_logic_tdd_clean_architecture_report.md](report/02_dual_track_ui_logic_tdd_clean_architecture_report.md) | §2.2 테이블, `UI-RED-*`, §0 PRD 정합 |
| 실행·ECB·엔티티 TDD 절차 예시 | [report/03_user_entity_ecb_tdd_implementation_report.md](report/03_user_entity_ecb_tdd_implementation_report.md) | ECB·pytest AAA·`entity` 샘플 |
| 에디터/에이전트 규칙 | [.cursorrules](.cursorrules) | ECB 방향, RED/GREEN/REFACTOR, pytest, coverage 최소값 |
| 빌드·의존성(추가 시) | `pyproject.toml` (프로젝트 루트) | **현재 없음.** 추가되면 Python 버전·`pytest`·커버리지 설정의 단일 기준으로 사용. |

**문서 관계(한 줄):** 요구사항의 **단일 진실 공급원**은 PRD와 DESIGN으로 두고, PRD·여정·설계 인덱스는 [report/04](report/04_prd_journey_architecture_export_report.md) §4~6에 정리한다. 프로젝트 진입 문서(`README.md`) 작성·문서 맵 내보내기는 [report/05](report/05_readme_project_export_report.md)에서 보고한다. PRD v2.1 개정 요약은 [report/06](report/06_dual_track_mlops_prd_update_report.md)을 본다. `docs/5_*` 등 별도 분리는 report/04 §6 권장과 같은 취지로 유지할 수 있다.

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

현재는 **`pyproject.toml` 없이** 예시 테스트만 있다. 의존성 설치 후 프로젝트 루트에서:

```powershell
python -m pip install pytest pytest-cov
python -m pytest tests/entity -q
```

`tests/entity/`의 테스트는 실행 시 `src`를 `sys.path`에 넣도록 되어 있다. `pyproject.toml`과 전체 패키지 레이아웃이 생기면 위 명령과 문구를 그 설정에 맞게 바꾼다.

---

## To-Do (PRD FR·Dual-Track 기반 — 완료 시 체크)

아래는 **PRD**를 주 소스로 한 구현·검증 단위이다. 상세 ID·AC는 PRD 본문이 우선한다.

### Epic-001 — 4×4 마방진 완성 시스템 (Dual-Track, ECB)

- [ ] **E1-Track-A (Boundary):** FR-01 — 원시 `int[][]`에서 4×4, 빈칸 2, 0/1~16, 비0 중복 검증; 실패 시 `UI_*`·고정 `message`·**도메인 `solve` 미호출** (AC-05)  
- [ ] **E1-Track-B (Domain):** FR-02~05 — row-major 빈칸, 누락 두 수, `MagicSquare` 판정(34), 시도1→시도2·`int[6]`·`DOMAIN_NOT_MAGIC` (경계는 `UI_DOMAIN_FAILURE`로 매핑)  
- [ ] **E1-Entity/VO:** 4×4 보드(복사·불변)·`Position`(1-index)·`MissingNumbers` 등 (DESIGN, NFR-04)  
- [ ] **E1-Control:** 경계 통과 시에만 use case로 검증·탐색·솔버 순서 조율 — **규칙은 Entity/Domain Service에**  
- [ ] **E1-품질:** NFR-01~04, PRD `§8`·`§9` TC(`UI-RED-*`, `D-RED-*`, `TP-OK/TP-FAIL`) 및 Traceability `§12`  
- [ ] **E1-리팩터:** 두 트랙 테스트가 모두 Green일 때만 구조 정리(`.cursorrules` `refactor_phase`)  

### 세부 작업(체크리스트, PRD 기능과 대응)

- [ ] **T-FR-01** 입력 검증(Boundary + 필요 시 Domain 중복 경로) — [FR-01](docs/PRD_magic_square_4x4_tdd.md)  
- [ ] **T-FR-02** 빈칸 탐지(row-major, 1-index) — [FR-02](docs/PRD_magic_square_4x4_tdd.md)  
- [ ] **T-FR-03** 누락 숫자 2개·`small`/`large` — [FR-03](docs/PRD_magic_square_4x4_tdd.md)  
- [ ] **T-FR-04** 완전 격자 마방진 판정(합 34) — [FR-04](docs/PRD_magic_square_4x4_tdd.md)  
- [ ] **T-FR-05** 두 조합 시도, `int[6]` 반환·실패 시 도메인/경계 코드 — [FR-05](docs/PRD_magic_square_4x4_tdd.md)  
- [ ] **T-잘못된 입력** 3×4, 빈칸 1·3, 범위 초과, 중복(TP-FAIL, PRD §9)  
- [ ] **T-커버리지** Domain ≥95%, Boundary ≥85%, 회귀 시 TC ID 삭제 금지(정책은 PRD §9.3)  

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
- [Report/2 — 경계·계약](report/02_dual_track_ui_logic_tdd_clean_architecture_report.md)  
- [Report/3 — ECB·TDD 예시](report/03_user_entity_ecb_tdd_implementation_report.md)  
- [`.cursorrules`](.cursorrules)  
