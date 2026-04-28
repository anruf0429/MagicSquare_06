# README·문서 맵·To-Do 산출물 내보내기 보고서

본 문서는 Magic Square(4×4) TDD 연습 저장소에서 수행한 **프로젝트 진입 문서(`README.md`) 작성 및 문서 간 참조 관계 정리** 작업 결과를 보고서 형태로 내보낸 것이다. 도메인 솔버·경계 구현 코드 자체는 본 보고서 범위에 포함하지 않으며, **온보딩·추적성·체크리스트**에 초점을 둔다.

| 항목 | 내용 |
|------|------|
| 보고서 버전 | 1.2 |
| 상태 | 산출물 인덱스·내보내기 |
| 근거 문서 | `docs/PRD_magic_square_4x4_tdd.md`(v2.1), `docs/DESIGN_layered_architecture_tdd_magic_square_4x4.md`, `report/01_*`, `report/02_*`, `report/03_*`, `report/04_*`, `report/06_*`, `.cursorrules`, 현재 `README.md` |

---

## 1) 작업 목적

- 저장소 루트에 **단일 진입점 문서**를 두어, 구현자·리뷰어가 **PRD 중심의 요구·검증·To-Do**를 한 화면에서 찾을 수 있게 한다.
- **Report/4**에 요약된 Epic·Journey·User Story 표현과 **Report/2**의 경계 계약(`UI_*`)·**Report/3** 및 `.cursorrules`의 ECB·TDD·실행 규칙을 README 수준에서 **재연결**한다.
- `report/04` §6에서 언급한 **문서 인덱스·후속 분리** 역할의 일부를 `report/05`(본 문서) 및 **`README.md`**로 구체화한다.

---

## 2) 산출물 목록

| 구분 | 경로 | 설명 |
|------|------|------|
| 프로젝트 진입·To-Do | `README.md` | 프로젝트 요약, **저장소 스냅샷**(문서 v2.1·구현·`pyproject.toml` 유무), 문서 근거 표(Report/1 포함), 도메인 요약, `UI_*` 표, User Story(Report/4 정합), NFR 검증 요약, ECB·pytest 실행 안내(`tests/entity` 예시), Epic/FR 단위 To-Do 체크리스트, 참고 링크 |
| 본 내보내기 보고서 | `report/05_readme_project_export_report.md` | README 작성 배경·목적·관련 문서 관계·후속 권장 |

기존 산출물과의 관계는 다음과 같다.

| 문서 | 역할 |
|------|------|
| `report/01_problem_definition_report.md` | 문제 인식·Invariant 개념 |
| `report/02_dual_track_ui_logic_tdd_clean_architecture_report.md` | Dual-Track·경계 계약·`UI_*`/메시지 |
| `report/03_user_entity_ecb_tdd_implementation_report.md` | ECB·pytest AAA·User 엔티티 구현 예시 |
| `report/04_prd_journey_architecture_export_report.md` | PRD·여정·설계 산출 **인덱스**, Epic/Journey/Story 요약 |
| **본 보고서 (`05_*`)** | **`README.md` 작업** 및 프로젝트 문서 **온보딩 내보내기** |
| `report/06_dual_track_mlops_prd_update_report.md` | PRD v2.1·Dual-Track/MLOps 정렬 **갱신 이력** |

---

## 3) README 본문 구조 (요약)

`README.md`는 다음 섹션으로 구성된다.

| 섹션 | 내용 | 주 근거 |
|------|------|---------|
| 도입 | 4×4 부분 빈칸 완성 목표, TDD·Invariant 강조 | PRD Executive Summary |
| 현재까지의 작업 | 요구·설계 문서 상태, FR-01~05 미구현·ECB `User` 예시만 존재, `pyproject.toml` 없음 | README와 저장소 정합(온보딩 투명성) |
| 문서·근거 표 | PRD, DESIGN, Report/1·2·3·4·5·6, `.cursorrules`, `pyproject.toml`(선택·현재 없음) | 사용자 요청 체계 |
| 문서 관계 한 줄 | PRD+DESIGN을 SSoT로, 인덱스는 Report/4; Report/5 분리 전까지 README·본 보고서로 보완 | Report/04 §6 권장과 정합 |
| 도메인 요약 | 4×4, 0 두 칸, 합 34, `int[6]`·1-index | PRD §5~6 |
| 경계 `UI_*` 표 | 고정 code/message | Report/02 §2.2, PRD §8.1; PRD §2.3·§9.1(UX Contract·매핑) |
| User Story 요약 | 검증·빈칸·누락·판정·두 조합 | Report/04 §3.3 |
| 검증 기준 | NFR-01~06, 커버리지·CI 게이트 | PRD §7·§7.1 |
| 실행·ECB·TDD | 의존 방향, pytest·AAA, Python 3.10+; 예: `python -m pytest tests/entity -q` | Report/03, `.cursorrules` |
| To-Do | Epic-001 Track-A/B, Entity, Control, 품질, T-FR-01~05 등 | PRD FR·Dual-Track |
| 참고 링크 | 위 문서 일괄 링크 | — |

**식별자 참고:** 대화·타 문서에서 `docs/5.PRD_MagicSquare_4x4_TDD.md`로 칭할 수 있으나, 본 저장소의 실제 PRD 경로는 **`docs/PRD_magic_square_4x4_tdd.md`** 이다. README에 해당 매핑을 명시한다.

---

## 4) 검증·완료 조건 (본 작업 기준)

| ID | 내용 | 상태 판단 |
|----|------|-----------|
| VE-01 | `README.md`가 존재하고 PRD를 중심 문서로 명시한다 | 파일 존재·내용 |
| VE-02 | Report/1·2·3·4·6 역할이 표 또는 본문으로 연결된다 | README 「문서·근거」 |
| VE-03 | To-Do가 PRD FR/NFR·Dual-Track과 대응 가능한 수준으로 체크리스트화된다 | README 「To-Do」 |
| VE-04 | 경계 `UI_*` 고정 메시지가 Report/2·PRD와 불일치하지 않는다 | 표 문자열 대조 |

구현 완료 여부(FR-01~05 코드)는 본 내보내기 작업의 완료 조건에 포함하지 않는다.

---

## 5) 후속 권장

- **`pyproject.toml`** 추가 시 README 「실행」절을 해당 파일의 Python 버전·`pytest`·커버리지 설정에 맞게 갱신하고, 필요하면 **`## 현재까지의 작업`** 표의 빌드 설정 행을「있음」으로 바꾼다.
- 마방진 도메인·경계 구현이 진행되면 **`README.md`의 To-Do 체크박스**와 저장소 스냅샷 표를 함께 갱신하거나, 세분화 시 `docs/TODO_*.md`로 분리할 수 있다.
- `report/04`와 본 보고서를 함께 두면 **문서 맵(PRD → DESIGN → Report 시리즈 → README)** 추적이 유지된다.

---

## 6) 참조 파일 경로

- `README.md`
- `docs/PRD_magic_square_4x4_tdd.md`
- `docs/DESIGN_layered_architecture_tdd_magic_square_4x4.md`
- `report/01_problem_definition_report.md`
- `report/02_dual_track_ui_logic_tdd_clean_architecture_report.md`
- `report/03_user_entity_ecb_tdd_implementation_report.md`
- `report/04_prd_journey_architecture_export_report.md`
- `report/06_dual_track_mlops_prd_update_report.md`
- `.cursorrules`
