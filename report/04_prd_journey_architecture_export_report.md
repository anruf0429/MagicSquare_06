# PRD·사용자 여정·계층 설계 산출물 정리 보고서

본 문서는 Magic Square(4×4) TDD 연습 프로젝트에 대해 **요구사항·사용자 여정·기술 시나리오·아키텍처/계약 설계**를 정리·문서화한 작업 결과를 보고서 형태로 내보낸 것이다. 구현 코드는 본 보고서 범위에 포함하지 않는다.

| 항목 | 내용 |
|------|------|
| 보고서 버전 | 1.1 |
| PRD 정합 | `docs/PRD_magic_square_4x4_tdd.md` **v2.1**(Dual-Track 언어·§7.1 CI·§9.1 매핑 등). 변경 요약은 `report/06_dual_track_mlops_prd_update_report.md` 참조. |

---

## 1) 작업 목적

- **비즈니스·학습 목표**를 Epic → Journey → User Story → Technical 시나리오 → 검증 체크리스트로 **추적 가능한 형태**로 정리한다.
- **PRD(제품 요구사항)**를 12개 섹션 구조(Executive Summary ~ Traceability)로 고정한다.
- **Dual-Track TDD(경계 / 도메인)**와 **Concept-to-Code Traceability**를 문서에 반영한다.
- **레이어 분리 + 계약 기반 테스트 + 리팩토링** 훈련을 위한 **설계·계약·테스트·통합 계획**을 `docs`에 별도 산출물로 둔다.

---

## 2) 산출물 목록

| 구분 | 경로 | 설명 |
|------|------|------|
| PRD | `docs/PRD_magic_square_4x4_tdd.md` | 12섹션 PRD(v2.1: §2.3 UX/Logic 언어·§7.1 CI/MLOps 정렬·§8.0/§8.4 Dual-Track·§9.1 시나리오 매핑·NFR-06·DEC-05 포함) |
| 계층 설계 | `docs/DESIGN_layered_architecture_tdd_magic_square_4x4.md` | Domain / Boundary / Data / Integration, API·테스트 ID·커버리지·Traceability |
| (대화·초안) | — | 아래 §3에 요약 기재: Epic, User Journey, User Stories, Gherkin 시나리오, Level 5 검증 체크리스트 |

`docs` 외에 **전용 마크다운 파일로 저장되지 않은** 서술(여정·스토리 등)은 §3에만 요약하며, 필요 시 동일 내용을 별도 파일로 분리할 수 있다.

---

## 3) 요구사항·여정·스토리 요약 (작업 중 정리된 내용)

### 3.1 Level 1 — Epic (비즈니스 목표)

| 항목 | 내용 |
|------|------|
| Epic | Invariant(불변조건) 기반 사고 훈련 시스템 구축 |
| 목적 | 4×4 Magic Square로 Invariant 중심 설계, Dual-Track TDD, 입출력 계약 명확화, 설계→테스트→구현→리팩토링 흐름 체화 |
| 성공 기준(예시) | Domain Logic 테스트 커버리지 95% 이상, 입력 검증 100% 계약 테스트, 하드코딩/매직 넘버 없음, Invariant→Test 추적 가능 |

### 3.2 Level 2 — User Journey

| Persona | TDD 훈련 중, Clean Architecture 이해 중인 소프트웨어 개발 학습자 |
|---------|-------------------------------------------------------------------|
| Step 1 | “마방진을 구현”이 아니라 Invariant·계약 중심 문제 인식 |
| Step 2 | 입력/출력 스키마·예외 정책 정의 |
| Step 3 | Domain 분리(빈칸·누락 수·판정·솔버 등) |
| Step 4 | Dual-Track: UI RED & Logic RED → GREEN → REFACTOR |
| Step 5 | 엣지·입력 오류·조합 실패 회귀 보호 |

### 3.3 Level 3 — User Stories (요지)

| Story | As / Want / So that (요지) |
|-------|-----------------------------|
| 1 | 입력 4×4·빈칸 2·범위·중복 검증 |
| 2 | 0의 좌표 row-major, 2개 |
| 3 | 1~16 누락 2개 오름차순 |
| 4 | 행·열·대각 합 동일(34) 판정 |
| 5 | 작은 수→첫 빈칸 시도, 실패 시 역배치, `int[6]`·1-index |

### 3.4 Level 4 — Technical 시나리오 (Gherkin 방향)

- **Background**: 4×4, 0=빈칸 2개, 1~16, 중복 없음, Magic Constant 34.
- **시나리오**: (1) 작은 수→큰 수 조합으로 완성, (2) 역배치로만 완성, (3) 빈칸 개수 오류, (4) 중복, (5) 범위 초과.
- 대표 격자는 PRD `§9.4` 데이터셋 A와 정합.

### 3.5 Level 5 — 시나리오 검증·정리

- 4레벨 일관성(Epic↔Journey↔Story↔Technical), 엣지·정상·예외 커버리지, 구현 가능성, Traceability 점검 항목을 체크리스트로 정리(일부 항목은 Magic Square 범위에 맞게 N/A 또는 대체).

---

## 4) PRD·설계서의 핵심 고정 사항

### 4.1 입력·출력 계약 (PRD·DESIGN 공통)

| 구분 | 고정 내용 |
|------|-----------|
| 입력 | `int[][]` 4×4, `0`은 빈칸 정확히 2개, 값은 0 또는 1~16, 0 제외 중복 없음, 첫 빈칸=row-major 첫 `0` |
| 출력 | `int[6]` = `[r1,c1,n1,r2,c2,n2]`, 좌표 1~4 **1-index** |
| 솔브 순서 | 시도1: `small`→첫 빈칸, `large`→둘째 빈칸 → 마방진이면 반환. 아니면 시도2: `large`→첫, `small`→둘째 → 마방진이면 반환. 둘 다 아니면 `DOMAIN_NOT_MAGIC` / 경계 `UI_DOMAIN_FAILURE` 및 고정 메시지 |
| Magic Constant | **34** |

### 4.2 Dual-Track·추적성

- **Track A (Boundary / UX Contract)**: 그래픽 UI가 아니라 **호출자·테스트가 관측하는 출력 계약** — 입력 검증, 고정 `UI_*` 코드·message, Domain 미호출 조건(PRD §2.3, §8.0).
- **Track B (Logic Rule)**: Domain — INV·마방진 판정·두 조합, `D-RED-*` 테스트.
- **시나리오 매핑**: 시나리오 ↔ UX Contract ↔ Logic Rule 표는 PRD **§9.1**.
- **진입 정책**: 통합 경로 Boundary(FR-01) 선행; 솔버 내부 재검증 (a)/(b) 택1은 PRD **§8.4·DEC-05**.
- **Traceability**: Concept / Invariant → Business Rule → FR → AC → Test Case → Component (`PRD` §12, `DESIGN` §4.5).

### 4.3 비기능·품질

- Domain ≥95%, Boundary ≥85%, Data ≥80% 커버리지 목표(PR·설계서 기준).
- **NFR-06**: 위 커버리지 하한 미달 시 **CI 파이프라인 실패**(PRD §7, §7.1).
- 동일 입력→동일 출력(결정론), 원본 행렬 비변조(NFR 명시).
- `.cursorrules`: ECB, pytest AAA, TDD 단계 규칙.

---

## 5) 기존 report 문서와의 관계

| 문서 | 역할 |
|------|------|
| `report/01_problem_definition_report.md` | 문제 인식·Invariant 개념 |
| `report/02_dual_track_ui_logic_tdd_clean_architecture_report.md` | Dual-Track·계약·통합(본 작업 PRD/DESIGN과 정합) |
| `report/03_user_entity_ecb_tdd_implementation_report.md` | User 엔티티 ECB/TDD 구현 보고 |
| **본 보고서 (`04_…`)** | PRD·여정·설계 산출물 **내보내기·인덱스** |
| `report/06_dual_track_mlops_prd_update_report.md` | PRD v2.1 개정·Dual-Track/MLOps 정렬 **변경 이력** |

---

## 6) 결론 및 후속 권장

- 요구사항의 **단일 진실 공급원**은 `docs/PRD_magic_square_4x4_tdd.md`와 `docs/DESIGN_layered_architecture_tdd_magic_square_4x4.md`로 둔다.
- Epic·Journey·Story·Level4~5 서술을 **저장 파일**로도 유지하려면 `docs/` 또는 `report/`에 `05_user_journey_stories.md` 등으로 분리 편집할 수 있다.
- 구현 단계에서는 PRD의 **FR-01~05 AC**와 설계서의 **TC ID**를 그대로 테스트 이름·ID에 매핑하면 추적성이 유지된다.

---

## 부록) 참조 파일 경로

- `docs/PRD_magic_square_4x4_tdd.md`
- `docs/DESIGN_layered_architecture_tdd_magic_square_4x4.md`
- `report/01_problem_definition_report.md`
- `report/02_dual_track_ui_logic_tdd_clean_architecture_report.md`
- `report/03_user_entity_ecb_tdd_implementation_report.md`
- `report/06_dual_track_mlops_prd_update_report.md`
- `.cursorrules`
