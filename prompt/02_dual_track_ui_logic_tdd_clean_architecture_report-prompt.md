# Magic Square TDD design and architecture
_Exported on 4/27/2026 at 16:57:24 GMT+9 from Cursor (3.2.11)_

---

**User**

당신은 Dual-Track UI + Logic TDD 및 Clean Architecture 설계 전문가입니다.

프로젝트: Magic Square (4x4) — TDD 연습용
목적: 알고리즘 난이도보다 “레이어 분리 + 계약 기반 테스트 + 리팩토링” 훈련
제약:
- 구현 코드는 작성하지 마십시오. (설계/계약/테스트/통합 계획만)
- UI는 실제 화면이 아니라 “입력/출력 경계(Boundary)”로 정의
- Data Layer는 DB가 아니라 “저장/로드 인터페이스(메모리/파일 교체 가능)” 수준만
- 입력/출력은 명확히 고정

입력 계약:
- 4x4 int\\\[]\\\[] (0은 빈칸)
- 빈칸은 정확히 2개
- 값 범위: 0 또는 1\\\~16
- 0 제외 중복 금지
출력 계약:
- int\\\[6]
- 좌표는 1-index
- 반환 형식: \\\[r1,c1,n1,r2,c2,n2]
- n1,n2는 두 누락 숫자이며, (작은수→첫빈칸, 큰수→둘째빈칸) 조합이 마방진이면 그 순서로, 아니면 반대로

------------------------------------------------------------
출력 형식 (반드시 이 구조로)
------------------------------------------------------------

# 1) Logic Layer (Domain Layer) 설계
## 1.1 도메인 개념
- Entities / Value Objects / Domain Services 목록과 책임(SRP)
## 1.2 도메인 불변조건(Invariants)
- 행/열/대각선 합 일치, Magic Constant 등
## 1.3 핵심 유스케이스(도메인 관점)
- 빈칸 찾기, 누락 숫자 찾기, 마방진 판정, 두 조합 시도
## 1.4 Domain API(내부 계약)
- 메서드 시그니처 수준(코드 X) + 입력/출력/실패조건
## 1.5 Domain 단위 테스트 설계(RED 우선)
- 테스트 케이스 목록(정상/비정상/엣지)
- 각 테스트가 보호하는 invariant 명시

# 2) Screen Layer (UI Layer) 설계 (Boundary Layer)
## 2.1 사용자/호출자 관점 시나리오
- “행렬 입력 → 검증 → 결과 출력” 흐름
## 2.2 UI 계약(외부 계약)
- Input schema / Output schema / Error schema
## 2.3 UI 레벨 테스트(Contract-first, RED 우선)
- 잘못된 크기, 빈칸 개수 오류, 값 범위 오류, 중복 오류, 반환 포맷 검증
- Domain은 Mock으로 가정
## 2.4 UX/출력 규칙
- 에러 메시지 표준(정확한 문구 규칙까지)

# 3) Data Layer 설계 (Data Layer)
## 3.1 목적 정의
- “저장/로드”의 필요성과 범위(학습용)
## 3.2 인터페이스 계약
- 예: MatrixRepository.save/load (메서드 수준, 코드 X)
- 저장 대상: 입력 행렬, 실행 결과(선택)
## 3.3 구현 옵션 비교(메모리/파일)
- 옵션 A: InMemory / 옵션 B: File(JSON/CSV)
- 추천안 1개 선택 + 이유
## 3.4 Data 레이어 테스트
- 저장/로드 정합성, 예외(파일 없음/형식 오류), 불변조건(4x4 유지)

# 4) Integration \\\& Verification (통합 및 검증)
## 4.1 통합 경로 정의
- UI → Application(선택) → Domain → Data 흐름(의존성 방향 포함)
## 4.2 통합 테스트 시나리오
- 정상 시나리오 2개 이상
- 실패 시나리오 3개 이상(입력 오류, 도메인 실패, 데이터 실패)
## 4.3 회귀 보호 규칙
- 기존 테스트 유지 정책
- 변경 금지 규칙(계약/출력 포맷)
## 4.4 커버리지 목표
- Domain Logic 95%+
- UI Boundary 85%+
- Data 80%+
## 4.5 Traceability Matrix (필수)
- Concept(Invariant) → Rule → Use Case → Contract → Test → Component

------------------------------------------------------------
추가 조건
------------------------------------------------------------
- 모호한 표현 금지(“적절히/충분히” 금지)
- 모든 규칙은 검증 가능해야 함(테스트로 확인 가능)
- 구현 코드 작성 금지
- 표/체크리스트를 적극 사용


---

**Cursor**

요청하신 산출물은 아키텍처/계약/테스트 중심의 분석 아티팩트라서, 먼저 관련 스킬 지침을 확인한 뒤 그 형식에 맞춰 정확한 구조로 설계를 작성하겠습니다.

요구하신 형식을 그대로 담은 설계 아티팩트를 캔버스로 작성하겠습니다. 지금 `Logic/UI/Data/Integration` 전 섹션과 추적성 매트릭스를 표/체크리스트 중심으로 정리해 파일로 생성합니다.

요청하신 산출물을 캔버스로 생성했습니다:  
`C:\Users\usejen_id\.cursor\projects\c-DEV-MagicSquare\canvases\magic-square-dual-track-design.canvas.tsx`

캔버스는 채팅 옆에서 여는 “독립 문서형 결과물”이고, 이번 요청처럼 표/체크리스트/추적성 매트릭스가 많은 설계를 한눈에 검토하기에 적합해서 이 형식을 사용했습니다.

# 1) Logic Layer (Domain Layer) 설계
## 1.1 도메인 개념
- `Matrix4x4`(Entity): 4x4 상태/좌표 접근 책임.
- `Position`(VO): 1-index 좌표(`r,c` in `1..4`).
- `MissingNumbers`(VO): 누락 숫자 2개(오름차순 보장).
- `InputValidator`(Service): 크기/빈칸/범위/중복 검증.
- `MagicSquareJudge`(Service): 행/열/대각선 합=34 판정.
- `FillStrategy`(Service): 두 조합 시도 및 규칙 기반 선택.

## 1.2 도메인 불변조건(Invariants)
- `INV-01`: 행렬 크기 `4x4`.
- `INV-02`: 빈칸(`0`) 개수 정확히 `2`.
- `INV-03`: 값 범위 `0` 또는 `1..16`.
- `INV-04`: `0` 제외 중복 금지.
- `INV-05`: 누락 숫자 개수 정확히 `2`.
- `INV-06`: 행/열/주/부대각선 합 모두 `34`.

## 1.3 핵심 유스케이스(도메인 관점)
- 빈칸 찾기(스캔 순서 고정).
- 누락 숫자 찾기(오름차순).
- 마방진 판정.
- `(small->blank1, large->blank2)` 먼저 시도, 실패 시 반대 조합 시도.
- 최종 반환 형식 `int[6]=[r1,c1,n1,r2,c2,n2]`.

## 1.4 Domain API(내부 계약)
- `validateInput(matrix:int[][]) -> ValidationResult`
- `findBlankPositions(matrix) -> Position[2]`
- `findMissingNumbers(matrix) -> {small:int, large:int}`
- `isMagicSquare(matrix) -> boolean`
- `solveTwoBlanks(matrix) -> int[6]`
- 실패는 코드로 고정(`DOMAIN_INVALID_SIZE`, `DOMAIN_INVALID_BLANK_COUNT`, `DOMAIN_OUT_OF_RANGE`, `DOMAIN_DUPLICATE_NONZERO`, `DOMAIN_INVALID_MISSING_COUNT`, `DOMAIN_NOT_MAGIC`).

## 1.5 Domain 단위 테스트 설계(RED 우선)
- 정상: 유효 입력에서 `int[6]` 반환 + 규칙 순서 검증.
- 비정상: 크기 오류/빈칸 개수 오류/범위 오류/중복 오류.
- 엣지: 누락 숫자 개수 오류, 두 조합 모두 실패.
- 각 테스트는 `INV-01~06` 중 최소 1개를 명시적으로 보호.

# 2) Screen Layer (UI Layer) 설계 (Boundary Layer)
## 2.1 사용자/호출자 관점 시나리오
- 행렬 입력 -> UI 계약 검증 -> Domain 호출 -> 결과 포맷 반환.
- 계약 실패 시 Domain 미호출.

## 2.2 UI 계약(외부 계약)
- Input schema: `{ matrix: int[4][4] }`
- Output schema: `{ result: int[6] }`
- Error schema: `{ code: string, message: string, details?: string[] }`

## 2.3 UI 레벨 테스트(Contract-first, RED 우선)
- 잘못된 크기 -> `UI_INVALID_SIZE`.
- 빈칸 개수 오류 -> `UI_INVALID_BLANK_COUNT`.
- 값 범위 오류 -> `UI_OUT_OF_RANGE`.
- 중복 오류 -> `UI_DUPLICATE_NONZERO`.
- 반환 포맷 검증 -> 길이 6, 좌표 1-index, 순서 `[r1,c1,n1,r2,c2,n2]`.
- Domain은 Mock으로 분리(성공/실패 매핑만 검증).

## 2.4 UX/출력 규칙
- 에러 메시지 고정 규칙:
  - `matrix must be 4x4`
  - `matrix must contain exactly two zeros`
  - `values must be 0 or in [1,16]`
  - `non-zero values must be unique`
  - `no valid magic-square completion found`
- `code`는 대문자 스네이크케이스 고정.
- 성공 응답은 `result` 필드만 포함.

# 3) Data Layer 설계 (Data Layer)
## 3.1 목적 정의
- 학습 범위: 저장/로드 인터페이스 분리와 교체 가능성 검증.
- 비범위: DB, 트랜잭션, 동시성 제어.

## 3.2 인터페이스 계약
- `saveInput(runId, matrix)` / `loadInput(runId)`
- `saveResult(runId, result)` / `loadResult(runId)` (선택 저장)
- 데이터 불변조건: 입력은 `4x4`, 결과는 `int[6]`.

## 3.3 구현 옵션 비교(메모리/파일)
- 옵션 A InMemory: 빠름, 단위 테스트 최적, 지속성 없음.
- 옵션 B File(JSON/CSV): 재현성 높음, I/O/파싱 예외 처리 필요.
- 추천: **InMemory 기본 + File 대체 구현 유지**(TDD 속도와 교체성 동시 확보).

## 3.4 Data 레이어 테스트
- 저장/로드 정합성(동일성).
- 파일 없음(`DATA_NOT_FOUND`), 형식 오류(`DATA_FORMAT_INVALID`).
- 불변조건 위반(`DATA_INVARIANT_VIOLATION`) 시 실패.

# 4) Integration & Verification (통합 및 검증)
## 4.1 통합 경로 정의
- `UI -> Application(선택) -> Domain -> Data(Port)`
- Domain은 UI/Data 구현 세부사항에 의존 금지.

## 4.2 통합 테스트 시나리오
- 정상 2개 이상:
  - 유효 입력 A 성공.
  - 유효 입력 B(역조합만 성립) 성공.
- 실패 3개 이상:
  - 입력 계약 실패(UI 단계 차단).
  - 도메인 해 없음.
  - 데이터 저장/로드 실패.

## 4.3 회귀 보호 규칙
- 기존 RED 테스트 삭제 금지.
- 입력/출력 계약 문자열/포맷 변경 금지.
- 좌표 1-index 규칙 변경 금지.
- Invariant 테스트 스위트 상시 실행.

## 4.4 커버리지 목표
- Domain Logic `95%+`
- UI Boundary `85%+`
- Data `80%+`

## 4.5 Traceability Matrix (필수)
- 캔버스에 `Concept(Invariant) -> Rule -> Use Case -> Contract -> Test -> Component` 전체 매핑을 완전 표로 작성해 두었습니다.
- `INV-01~06`, 출력 계약, 데이터 불변조건까지 모두 테스트 ID와 컴포넌트에 연결했습니다.

원하시면 다음 답변에서 이 캔버스 내용을 그대로 `report/` 아래 Markdown 문서(`TDD 설계서`)로도 변환해 드리겠습니다.

---

**User**

report  폴더에 지금 작업한 내용을 보고서로 내보내줘

---

**Cursor**

캔버스에 정리한 설계를 `report` 폴더용 Markdown 보고서로 바로 내보내겠습니다. 먼저 기존 보고서 형식을 확인한 뒤 같은 톤으로 새 파일을 생성할게요.

기존 보고서 네이밍을 맞춰 `report`에 새 Markdown 파일을 추가하겠습니다. 캔버스 내용을 그대로 옮기되, 검증 가능한 규칙/체크리스트/매트릭스 중심으로 구성하겠습니다.

내보내기 완료했습니다.  
`report` 폴더에 아래 파일로 저장해두었습니다.

- `C:\DEV\MagicSquare\report\02_dual_track_ui_logic_tdd_clean_architecture_report.md`

캔버스에서 정리한 내용을 그대로 보고서 형태로 옮겼고, 요청하신 1~4번 구조/체크리스트/Traceability Matrix까지 포함되어 있습니다.

