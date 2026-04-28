# Dual-Track UI + Logic TDD · MLOps 정렬 및 PRD 갱신 보고서

본 문서는 Magic Square(4×4) TDD 연습 프로젝트에 대해 **Dual-Track TDD를 UX Contract / Logic Rule 언어로 정리**, **MLOps에 대응 가능한 품질·CI 축을 PRD에 반영**, **`docs/PRD_magic_square_4x4_tdd.md`를 v2.1로 개정**한 작업 결과를 보고서 형태로 내보낸 것이다. 구현 코드 변경은 본 보고서 범위에 포함하지 않는다.

| 항목 | 내용 |
|------|------|
| 보고서 버전 | 1.0 |
| 상태 | 산출물 기록 |
| 근거 문서 | `docs/PRD_magic_square_4x4_tdd.md`(v2.1), `docs/DESIGN_layered_architecture_tdd_magic_square_4x4.md`, `report/02_dual_track_ui_logic_tdd_clean_architecture_report.md`, `report/04_prd_journey_architecture_export_report.md` |

---

## 1) 작업 배경

- 슬라이드 기반 방법론에 따라 **UI 트랙은 계약(경계 관측 가능 출력)으로 RED**, **로직 트랙은 규칙(BR·도메인)으로 RED**를 만든다는 원칙을 문서에 명시할 필요가 있었다.
- 그래픽 UI가 없는 본 프로젝트에서 **`UI_*` 접두어가 “픽셀 UI”로 오해되지 않도록** Boundary·UX Contract로 정의해야 했다.
- **MLOps**와의 정렬은 모델 학습 파이프라인이 아니라 **계약·결정론·커버리지 게이트·재현 가능한 산출물**로 서술할 필요가 있었다.
- PRD와 `report/02`·`report/04` 간 **절 번호·용어**를 최신화할 필요가 있었다.

---

## 2) PRD(`docs/PRD_magic_square_4x4_tdd.md`) 개정 요약 (v2.0 → v2.1)

| 구분 | 추가·변경 내용 |
|------|----------------|
| **§1 Executive Summary** | 경계 UX Contract·도메인 Logic Rule 언어(§2.3), CI 품질 게이트(§7.1) 고정을 한 문장으로 연결. |
| **§2.3 (신설)** | Dual-Track 언어: UX Contract / Logic Rule 예시 표; `UI_*`는 API·CLI·테스트 관측 표현임을 명시. **테스트 후보 선별**(이진 결정 있는 시나리오만 RED) 규칙. |
| **§7** | **NFR-06**: CI에서 NFR-01·NFR-02 미달 시 파이프라인 실패. NFR-05 검증 방법 열 보완. |
| **§7.1 (신설)** | **CI · 산출물 (MLOps 정렬)**: 학습 파이프 없음 명시, 권장 단계(정적 검사 → 도메인 테스트 → 경계·IT → 커버리지), 아티팩트(리포트·로그). |
| **§8.0 (신설)** | Track A/B 정의, 슬라이드 원칙과 동일한 한 줄(경계로 RED / 규칙으로 RED, GREEN·REFACTOR는 함께). |
| **§8.3** | 항목 5: 테스트 케이스 전환 시 §2.3 준수. |
| **§8.4 (신설)** | Boundary 우선·도메인 단위 테스트의 역할; 솔버 내부 재검증 (a)/(b) **택1** 및 DESIGN 문서와 정합. |
| **§9.1 (신설)** | **UX Contract · Logic Rule · 시나리오 매핑** 표(이진 결정 시나리오). |
| **§9.2~§9.5** | 기존 §9.1~§9.4가 한 단계씩 뒤로 이동(시나리오 목록, 회귀, 데이터셋, Property). |
| **§10.3** | §8.4와 솔버 재검증 정책 연결 문장. |
| **§11 DEC** | **DEC-05**: 통합 경로 Boundary 선행 불변; (a)/(b) 단일 선택 및 IT 검증. |

---

## 3) 기존 report·_DESIGN_와의 관계

| 문서 | 본 개정과의 관계 |
|------|------------------|
| `report/02_*` | Boundary/UI 설계와 PRD §2.3·§8.4 용어를 정합시키기 위해 **§0 보완 절**을 추가했다. |
| `report/04_*` | PRD v2.1·새 절 번호·NFR-06·매핑 표를 인덱스에 반영했다. |
| `report/05_*` | 문서 맵에 본 보고서(`06`)를 연결했다. |
| `docs/DESIGN_*` | PRD §8.4에서 설계서와 진입 정책 정합을 명시(별도 DESIGN 개정은 필수 아님). |

---

## 4) 결론 및 후속 권장

- **단일 진실 공급원**은 계속 `docs/PRD_magic_square_4x4_tdd.md`와 `docs/DESIGN_layered_architecture_tdd_magic_square_4x4.md`이다.
- CI를 도입할 때는 PRD **§7.1·NFR-06**에 맞춰 커버리지 게이트와 테스트 단계 순서를 설정한다.
- `README.md`의 NFR·문서 절 참조를 갱신할 때는 **§9.4**(데이터셋 A)·**§9.1**(매핑 표) 등 변경된 번호를 따른다.

---

## 5) 참조 파일 경로

- `docs/PRD_magic_square_4x4_tdd.md`
- `docs/DESIGN_layered_architecture_tdd_magic_square_4x4.md`
- `report/02_dual_track_ui_logic_tdd_clean_architecture_report.md`
- `report/04_prd_journey_architecture_export_report.md`
- `report/05_readme_project_export_report.md`
