# 소프트웨어 테스트 케이스 명세 내보내기 보고서

본 문서는 Magic Square(4×4) TDD 연습 저장소에 대해 **기능 모듈별 소프트웨어 테스트 케이스 명세**를 표준 필드 양식으로 정리한 산출물을 **보고서 형태로 내보낸** 것이다. 도메인 솔버·경계의 **구현 코드**는 본 보고서 범위에 포함하지 않으며, **테스트 ID·목적·입력·절차·성공·실패 기준**의 추적 가능성에 초점을 둔다.

| 항목 | 내용 |
|------|------|
| 보고서 버전 | 1.0 |
| 상태 | 산출물 인덱스·내보내기 |
| 근거 문서 | `docs/PRD_magic_square_4x4_tdd.md`(v2.1), `docs/DESIGN_layered_architecture_tdd_magic_square_4x4.md`, `docs/test_case_specification_magic_square_4x4.md`, `report/02_*`, `report/04_*` |

---

## 1) 작업 배경

- 마방진 도메인에 대해 **빈칸 좌표 탐색**, **완성 여부 검증**, **해 도출(빈칸 채우기)**, **경계값**, **오류·예외**를 구분한 테스트 항목을 한 문서로 묶을 필요가 있었다.
- 각 항목을 **프로젝트명·대상 시스템·테스트 ID·목적·기능·입력값·Given/When/Then·환경·전제 조건·성공/실패 기준** 등 공통 필드로 기술하면, PRD의 FR/NFR·경계 `UI_*`와 **대응 관계를 잡기 쉽다**.
- 좌표 표기(0-index vs 1-index)·예외 타입(`ValueError`, `TypeError` 등)은 **PRD·DESIGN에서 확정한 계약**과 정합을 유지해야 하므로, 명세 본문에 “설계에 따름” 등의 주석을 두었다.

---

## 2) 산출물 목록

| 구분 | 경로 | 설명 |
|------|------|------|
| 테스트 케이스 명세 (본체) | `docs/test_case_specification_magic_square_4x4.md` | 문서 공통 정보, TC ID 요약 표, **TC-MS-A~D** 개별 섹션(24건) |
| 본 내보내기 보고서 | `report/07_test_case_specification_export_report.md` | 배경·산출물·범주·검증·후속 권장 |

---

## 3) 명세 범주·ID 체계 (요약)

| 접두 | 범주 | 건수 | 내용 (요지) |
|------|------|------|-------------|
| **TC-MS-A** | 빈칸 찾기 (`find_blank_coords` 등) | 5 | 정상 2칸, 모서리·첫/끝 행, 빈칸 0/1/3+ (경계·탐색 단위) |
| **TC-MS-B** | 마방진 검증 (`is_magic_square` 등) | 5 | 완성 참, 행·열·주·부 대각 불일치 시 거짓 |
| **TC-MS-C** | 해 도출·경계·상수 | 8 | 솔버 정상·다양한 빈칸, 이미 완성, min/max 값, 행·열·대각 합 34 |
| **TC-MS-D** | 오류·예외 | 6 | 범위 밖, 중복, 크기 불일치, None/빈 입력, 문자열, 불규칙 행 길이 |

**우선순위:** 명세에 P1·P2·P3를 두었으며, 구현·회귀 우선순위는 PRD NFR·팀 정책에 맞출 수 있다.

---

## 4) 기존 문서와의 관계

| 문서 | 본 명세와의 관계 |
|------|------------------|
| `docs/PRD_magic_square_4x4_tdd.md` | FR-01~05, 경계 메시지(`UI_*`), 빈칸 2개·합 34·출력 `int[6]` 등 **요구의 단일 기준** |
| `docs/DESIGN_layered_architecture_tdd_magic_square_4x4.md` | Boundary / Domain 계층에 TC를 매핑할 때 **어느 레이어에서 RED할지** 참고 |
| `report/02_*` | `UI_*`·Dual-Track 요약; D계열 TC와 **경계 계약** 연결 |
| `report/04_*` | Epic·시나리오·여정; TC ID는 **§9.1 등 추적 표**와 대응 가능 |
| `README.md` | NFR·문서 맵; 본 명세는 **구현 전 테스트 설계 산출물**로 위치 |

---

## 5) 검증·완료 조건 (본 내보내기 기준)

| ID | 내용 | 상태 판단 |
|----|------|-----------|
| VE-TC-01 | `docs/test_case_specification_magic_square_4x4.md`가 존재하고 TC-MS-A~D가 빠짐없이 기술된다 | 파일·목차 |
| VE-TC-02 | 각 TC에 목적·입력·Given/When/Then·성공·실패 기준이 있다 | 표본 검토 |
| VE-TC-03 | PRD의 도메인 상수(4×4, 합 34, 값 범위 등)와 모순되는 서술이 없다 | PRD 대조 |

자동 테스트 코드 존재 여부는 본 내보내기 작업의 완료 조건에 포함하지 않는다.

---

## 6) 결론 및 후속 권장

- 테스트 구현 시에는 PRD **§8·§12** 및 DESIGN의 **TC ID·계층**과 매핑표를 두고, 명세의 TC-ID를 **pytest 마커 또는 테스트 이름**에 반영하면 추적성이 유지된다.
- 좌표가 **1-index 출력**인지 행렬 인덱스가 **0-index**인지는 구현 단계에서 단일 규칙으로 고정하고, 명세의 예시 좌표를 그에 맞게 수정·보완한다.
- CI 도입 후에는 PRD **§7.1·NFR-06**에 맞춰 커버리지 게이트와 함께 **P1 TC 우선 실행** 등을 정할 수 있다.

---

## 7) 참조 파일 경로

- `docs/test_case_specification_magic_square_4x4.md`
- `docs/PRD_magic_square_4x4_tdd.md`
- `docs/DESIGN_layered_architecture_tdd_magic_square_4x4.md`
- `report/02_dual_track_ui_logic_tdd_clean_architecture_report.md`
- `report/04_prd_journey_architecture_export_report.md`
- `report/05_readme_project_export_report.md`
- `report/06_dual_track_mlops_prd_update_report.md`
