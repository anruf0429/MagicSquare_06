# Magic Square (4×4) — 레이어 분리·계약·테스트·통합 설계서

| 항목 | 내용 |
|------|------|
| 문서 목적 | 구현 코드 없이 **설계·계약·테스트·통합 계획만** 정의한다. |
| 프로젝트 목표 | 알고리즘 난이도보다 **레이어 분리 + 계약 기반 테스트 + 리팩토링** 훈련. |
| 근거 PRD | `docs/PRD_magic_square_4x4_tdd.md` |
| 관련 보고서 | `report/02_dual_track_ui_logic_tdd_clean_architecture_report.md` |

### 용어 고정

| 용어 | 정의 |
|------|------|
| UI / Screen | **실제 화면 아님.** 호출자-facing **입력·출력 경계(Boundary)**. |
| Data Layer | **DB 아님.** 저장·로드를 추상화한 **포트(인터페이스)**; InMemory·파일 구현체로 교체 가능. |

---

## 고정 계약 요약 (Normative)

### 입력 계약

| ID | 규칙 | 검증 가능 진술 |
|----|------|----------------|
| IC-01 | 형태 | `int[][]`, 행 개수=4, 각 행 길이=4. |
| IC-02 | 빈 칸 | 값 `0`인 셀 개수=정확히 2. |
| IC-03 | 범위 | 각 셀은 `0` 또는 `1` 이상 `16` 이하 정수. |
| IC-04 | 중복 | `0`을 제외한 값은 서로 다름. |
| IC-05 | 첫 빈 칸 | row-major(행 우선, 열 증가) 스캔에서 **가장 먼저 만나는** `0`이 첫 빈 칸. |
| IC-06 | 둘째 빈 칸 | 첫 빈칸 이후 row-major로 만나는 나머지 `0` 하나. |

### 출력 계약

| ID | 규칙 | 검증 가능 진술 |
|----|------|----------------|
| OC-01 | 길이 | `int[6]`. |
| OC-02 | 필드 순서 | `[r1,c1,n1,r2,c2,n2]`. |
| OC-03 | 좌표 체계 | `r1,c1,r2,c2`는 **1-index**, 허용 `{1,2,3,4}`. |
| OC-04 | 값 의미 | `(r1,c1)`=첫 빈 칸, `(r2,c2)`=둘째 빈 칸; `n1`·`n2`는 각 위치에 배치된 값. |
| OC-05 | 누락 수 | `n1`·`n2`는 집합 `{1,…,16}`에서 격자에 없는 두 수(누락)로부터 온다. |
| OC-06 | 시도 1 | `small`을 첫 빈칸, `large`를 둘째 빈칸에 넣은 완성 행렬이 마방진이면 **이 배치**를 반환. `small`·`large`는 누락 두 수의 오름차순 작은 값·큰 값. |
| OC-07 | 시도 2 | 시도 1이 마방진이 아니면 `large`→첫 빈칸, `small`→둘째 빈칸. 마방진이면 **이 배치**를 반환. |
| OC-08 | 시도 1 성공 시 | 시도 2를 수행하지 않는다. |
| OC-09 | Magic Constant | n=4일 때 합 **34** (행·열·주대각·부대각). |

### 도메인 실패(해 없음)

| 조건 | 도메인 코드 | 경계 매핑(표시) |
|------|-------------|-----------------|
| 시도 1·2 모두 비마방진 | `DOMAIN_NOT_MAGIC` | `UI_DOMAIN_FAILURE` |

---

# 1) Logic Layer (Domain Layer) 설계

## 1.1 도메인 개념

| 구분 | 이름(논리) | 책임(SRP) | 검증 기준(측정 가능) |
|------|------------|-----------|----------------------|
| Entity | `Matrix4x4` | 4×4 셀 상태 보관, 1-index 좌표로 셀 읽기/쓰기(복사본 기준) | 행=4, 각 열=4, 접근 좌표 ∈[1,4] 시에만 셀 반환 |
| Value Object | `Position` | 1-index `(r,c)` | `r,c` ∈ {1,2,3,4} |
| Value Object | `MissingNumbers` | 누락 2수, `small` < `large` | 항상 정수 2개, 대소 관계 고정 |
| Domain Service | `InputValidator` (도메인 경로용) | `INV-01`~`INV-04`/`INV-05` 선행 조건 검증 | 실패 시 도메인 실패 코드 1:1 |
| Domain Service | `BlankFinder` (논리명) | row-major로 `0` 위치 2개 | `Position` 2개, 순서 고정 |
| Domain Service | `MissingNumberFinder` (논리명) | 1~16 중 미등장 2수 | `MissingNumbers` |
| Domain Service | `MagicSquareJudge` (논리명) | 행·열·대각 합=34 판정 | `boolean` |
| Domain Service | `FillStrategy` / `TwoBlankSolver` (논리명) | 시도1→시도2, `int[6]` 구성 | OC-01~09 |

## 1.2 도메인 불변조건(Invariants)

| ID | 불변조건(항상 참) | 검증 규칙(관측 가능) | 실패 코드 |
|----|-------------------|----------------------|-----------|
| INV-01 | 행렬은 4×4 | 행 수=4 ∧ 각 행 길이=4 | `DOMAIN_INVALID_SIZE` |
| INV-02 | 빈 칸은 정확히 2 | `0` 개수=2 | `DOMAIN_INVALID_BLANK_COUNT` |
| INV-03 | 셀 값은 0 또는 1~16 | 위 범위 밖 금지 | `DOMAIN_OUT_OF_RANGE` |
| INV-04 | 0 제외 중복 없음 | 동일 값 2회 이상 금지 | `DOMAIN_DUPLICATE_NONZERO` |
| INV-05 | 1~16 중 미등장은 정확히 2개 | 집합 연산으로 개수=2 | `DOMAIN_INVALID_MISSING_COUNT` |
| INV-06 | 마방진이면 네 행·네 열·두 대각 합=34 | 합이 34가 아닌 선이 0개 | `DOMAIN_NOT_MAGIC` (해 없음·판정 false에 연동) |
| INV-MC | 4×4 마방진 합 상수 | Magic Constant=**34** | `MagicSquareJudge`와 정합 |

## 1.3 핵심 유스케이스(도메인 관점)

| UC ID | 유스케이스 | 입력(전제) | 출력 | 실패조건(관측) |
|-------|------------|------------|------|----------------|
| UC-D-01 | 빈칸 찾기 | `INV-01`~`04` 만족 | `Position[2]` row-major | `INV-02` |
| UC-D-02 | 누락 숫자 찾기 | 위 동일 | `MissingNumbers` | `INV-05` |
| UC-D-03 | 마방진 판정 | 완전 채움(0 없음) 4×4, 1~16 | `boolean` | 값 위반 시 선행 검증 실패 |
| UC-D-04 | 두 조합 시도 | 빈칸 2·누락 2 확정 | 성공 시 배치, 실패 시 에러 코드 | 시도1·2 모두 비마방진 → `INV-06` |
| UC-D-05 | 출력 포맷 구성 | UC-D-04 성공 | `int[6]` | 길이≠6 또는 좌표 범위 위반 시 실패 |

## 1.4 Domain API(내부 계약)

구현 코드 없이 **이름·입력·출력·실패**만 규정한다.

| API (논리 이름) | 입력 | 출력 | 실패조건(코드) |
|-----------------|------|------|----------------|
| `validateInput` | `int[][]` | 성공/실패 + `errorCode` | `INV-01`~`INV-04` |
| `findBlankPositions` | 검증된 `Matrix4x4` 또는 동치 | `Position` 길이 2 | `INV-02` |
| `findMissingNumbers` | 동상 | `MissingNumbers` | `INV-05` |
| `isMagicSquare` | 0 없는 4×4 | `boolean` | 입력 불만족 시 선행 검증 |
| `solveTwoBlanks` | `int[][]` (경계 통과 후 또는 도메인 단독 진입 시 검증 포함 정책 택1) | 성공: `int[6]` / 실패: `errorCode` | 검증 실패 코드 또는 `DOMAIN_NOT_MAGIC` |

**정책 선택(명시)**: `solveTwoBlanks`는 (a) 호출 전 Boundary에서 이미 검증했다고 가정하거나, (b) 내부에서 `validateInput`을 한 번 더 호출한다. 프로젝트는 문서화된 한 가지를 택하고 통합 테스트가 그 전제를 검증한다.

**반환 순서 규칙(고정)**

| 순서 | 배치 | 다음 단계 |
|------|------|-----------|
| 1 | `small`→첫 빈칸, `large`→둘째 빈칸 | 마방진이면 `int[6]` 반환 및 종료 |
| 2 | `large`→첫 빈칸, `small`→둘째 빈칸 | 마방진이면 `int[6]` 반환 및 종료 |
| 3 | 둘 다 아님 | `DOMAIN_NOT_MAGIC` |

## 1.5 Domain 단위 테스트 설계(RED 우선)

### 테스트 케이스 목록

| TC ID | 유형 | Given | Expected | 보호 Invariant |
|-------|------|-------|----------|----------------|
| D-RED-01 | 정상 | 유효 행렬·해 존재 | `int[6]` 길이 6, 좌표 ∈[1,4], 합 34 | INV-01~06 |
| D-RED-02 | 비정상 | 3×4 또는 4×3 | `DOMAIN_INVALID_SIZE` | INV-01 |
| D-RED-03 | 비정상 | 빈칸 1 또는 3 | `DOMAIN_INVALID_BLANK_COUNT` | INV-02 |
| D-RED-04 | 비정상 | 값 17 | `DOMAIN_OUT_OF_RANGE` | INV-03 |
| D-RED-05 | 비정상 | 0 제외 중복 | `DOMAIN_DUPLICATE_NONZERO` | INV-04 |
| D-RED-06 | 엣지 | 누락 수 2개 아님 | `DOMAIN_INVALID_MISSING_COUNT` | INV-05 |
| D-RED-07 | 엣지 | 두 조합 모두 실패 | `DOMAIN_NOT_MAGIC` | INV-06 |
| D-RED-08 | 규칙 | 역조합만 마방진 | `int[6]`이 시도2 배치와 일치 | INV-06 + OC-06~07 |

### Domain RED 체크리스트

- [ ] 실패 `errorCode`가 위 표의 문자열과 **완전 일치**한다.
- [ ] 모든 성공 케이스에서 `int[6]` 길이=6.
- [ ] 좌표는 **1-index**로 단언한다.
- [ ] 시도1 성공 시 시도2 미호출을 스파이로 검증한다(선택·권장).

---

# 2) Screen Layer (UI Layer) 설계 — Boundary Layer

## 2.1 사용자/호출자 관점 시나리오

| 단계 | 행위 | 결과(관측) |
|------|------|------------|
| 1 | 호출자가 `matrix` 전달 | Boundary 수신 |
| 2 | Boundary가 입력 계약(IC-01~04) 검증 | 실패 시 **Domain 미호출** |
| 3 | 성공 시 Domain `solveTwoBlanks`(또는 Application 경유) 호출 | Domain 결과 수신 |
| 4 | 성공 시 Output schema로 `{ result: int[6] }` 반환 | 길이·좌표 검증 가능 |
| 5 | Domain 실패(`DOMAIN_NOT_MAGIC`) | `UI_DOMAIN_FAILURE` + 고정 메시지 |
| 6 | Data 저장 실패(선택 경로) | `UI_DATA_FAILURE` |

## 2.2 UI 계약(외부 계약)

### Input schema

| 필드 | 타입 | 제약 |
|------|------|------|
| `matrix` | `int[4][4]` | IC-01~04 |

### Output schema (성공)

| 필드 | 타입 | 제약 |
|------|------|------|
| `result` | `int[6]` | OC-01~04 |

### Error schema

| 필드 | 타입 | 제약 |
|------|------|------|
| `code` | 문자열 enum | 아래 표 집합만 |
| `message` | 문자열 | 아래 표와 **문자 단위 동일** |
| `details` | 문자열 배열, 선택 | 테스트 OPTIONAL |

| code | 발생 조건 | message (고정) |
|------|-----------|----------------|
| `UI_INVALID_SIZE` | 4×4 아님 | `matrix must be 4x4` |
| `UI_INVALID_BLANK_COUNT` | `0` 개수≠2 | `matrix must contain exactly two zeros` |
| `UI_OUT_OF_RANGE` | 값 범위 위반 | `values must be 0 or in [1,16]` |
| `UI_DUPLICATE_NONZERO` | 0 제외 중복 | `non-zero values must be unique` |
| `UI_DOMAIN_FAILURE` | 두 조합 실패 등 | `no valid magic-square completion found` |
| `UI_DATA_FAILURE` | 저장소 오류 | `data layer operation failed` |

## 2.3 UI 레벨 테스트(Contract-first, RED 우선)

**전제**: Domain은 Mock·Stub으로 대체하고 **호출 횟수·인자**를 검증한다.

| TC ID | 입력 | Domain Mock 동작 | Expected |
|-------|------|------------------|----------|
| UI-RED-01 | 3×4 행렬 | 호출 시 테스트 실패 | `UI_INVALID_SIZE`, Domain 호출 0회 |
| UI-RED-02 | 빈칸 3개 | 호출 시 테스트 실패 | `UI_INVALID_BLANK_COUNT`, 호출 0회 |
| UI-RED-03 | 값 18 포함 | 호출 시 테스트 실패 | `UI_OUT_OF_RANGE`, 호출 0회 |
| UI-RED-04 | 중복 | 호출 시 테스트 실패 | `UI_DUPLICATE_NONZERO`, 호출 0회 |
| UI-RED-05 | 유효 입력 | 고정 `int[6]` 반환 | Output schema 만족 |
| UI-RED-06 | 유효 입력 | Domain 실패 시뮬 | `UI_DOMAIN_FAILURE`, 고정 message |
| UI-RED-07 | 유효 입력 | 성공 반환 | `[r1,c1,n1,r2,c2,n2]` 순서 일치 |

## 2.4 UX/출력 규칙

| 규칙 ID | 규칙 | 테스트 방식 |
|---------|------|-------------|
| MSG-01 | `message`는 표의 문자열과 완전 일치 | Equality assertion |
| MSG-02 | `code`는 허용 enum만 | Membership assertion |
| MSG-03 | 동일 원인→동일 code·message | 동일 입력 반복 |
| OUT-01 | 성공 시 `result`만 필수(스키마 문서 기준) | 필드 키 존재 |
| OUT-02 | 실패 시 `code`,`message` 필수 | 키 존재 |

### Boundary 체크리스트

- [ ] 입력 검증 실패 시 Domain 미호출.
- [ ] 에러 문자열 하드코딩 값이 테스트에 등장.
- [ ] 성공 응답에서 `int[6]` 길이 위반 시 테스트 실패.

---

# 3) Data Layer 설계

## 3.1 목적 정의

| 항목 | 내용 |
|------|------|
| 목적 | 실행 간 **입력 재현·결과 비교**를 위해 저장·로드를 경계로 분리하고, 테스트에서 **InMemory / File**로 교체 가능하게 한다. |
| 범위 | **포트(인터페이스) 계약**과 불변조건, 실패 코드. |
| 비범위 | RDBMS, 네트워크, 분산 트랜잭션. |

## 3.2 인터페이스 계약

**예시 포트 이름**: `MatrixRunRepository` (또는 `MatrixRepository`). 메서드 수준 계약은 아래와 같다.

| 메서드 | 입력 | 출력 | 실패 코드 |
|--------|------|------|-----------|
| `saveInput(runId, matrix)` | `string`, `int[4][4]` | 없음(void 의미) | `DATA_WRITE_FAILED`, `DATA_INVARIANT_VIOLATION` |
| `loadInput(runId)` | `string` | `int[4][4]` | `DATA_NOT_FOUND`, `DATA_FORMAT_INVALID` |
| `saveResult(runId, result)` | `string`, `int[6]` | 없음 | 위와 동일 |
| `loadResult(runId)` | `string` | `int[6]` | 위와 동일 |

**저장 대상**

| 대상 | 필수 여부 |
|------|-----------|
| 입력 행렬 | 학습 시나리오에 따라 필수 또는 선택 |
| 실행 결과 `int[6]` | 선택 |

## 3.3 구현 옵션 비교(메모리/파일)

| 옵션 | 설명 | 장점 | 단점 |
|------|------|------|------|
| **A. InMemory** | 프로세스 내 `dict` 등으로 보관 | 테스트 빠름, 설정 없음 | 프로세스 종료 시 소실 |
| **B. File(JSON/CSV)** | 파일 경로에 직렬화 | 사람이 열어보기 쉬움 | 파일 없음·권한·손상 처리 필요 |

### 추천안

| 선택 | **옵션 A (InMemory)** |
|------|------------------------|
| 이유 | 학습 목표는 레이어 분리·계약 테스트이며 I/O 분기를 줄여 **TDD 루프 시간을 최소화**한다. |

## 3.4 Data 레이어 테스트

| TC ID | 구현체 | 시나리오 | Expected |
|-------|--------|----------|----------|
| DATA-01 | InMemory | save 후 동일 `runId` load | 바이트/값 동등 |
| DATA-02 | InMemory | 없는 `runId` load | `DATA_NOT_FOUND` |
| DATA-03 | File | 정상 JSON load | `int[4][4]` 복원 |
| DATA-04 | File | 파일 없음 | `DATA_NOT_FOUND` |
| DATA-05 | File | 손상 형식 | `DATA_FORMAT_INVALID` |
| DATA-06 | 공통 | 4×4 아닌 matrix save 시도 | `DATA_INVARIANT_VIOLATION` |
| DATA-07 | 공통 | 길이≠6 result save | `DATA_INVARIANT_VIOLATION` |

### Data 체크리스트

- [ ] save 시 4×4·`int[6]` 불변조건 강제.
- [ ] `NOT_FOUND`와 `FORMAT_INVALID` 구분.
- [ ] 동일 포트에 대해 InMemory↔File 교체 시 상위 통합 테스트 재실행 통과.

---

# 4) Integration & Verification (통합 및 검증)

## 4.1 통합 경로 정의

**호출 흐름(논리)**

`Boundary(UI)` → `Application`(선택) → `Domain` → `Data Port`(선택)

**의존성 방향**

| 레이어 | 허용 의존 | 금지 |
|--------|-----------|------|
| Boundary | Application 공개 API | Domain 구체 클래스 직접 조작 |
| Application | Domain API, Repository 포트 | File/InMemory 구체 타입 직접 참조 |
| Domain | Domain 타입만 | Boundary DTO, 파일 경로 |
| Data 구현체 | Repository 포트 | Domain 규칙 재구현(중복) 지양 |

## 4.2 통합 테스트 시나리오

### 정상(2개 이상)

| ID | 시나리오 | 검증 포인트 |
|----|----------|-------------|
| IT-OK-01 | 유효 입력 A | `int[6]`·합 34·시도1이 성공이면 시도2 미적용 |
| IT-OK-02 | 유효 입력 B(역조합만 성립) | 반환 `int[6]`이 시도2 배치와 일치 |

### 실패(3개 이상)

| ID | 시나리오 | Expected |
|----|----------|----------|
| IT-FAIL-01 | 입력 크기 오류 | `UI_INVALID_SIZE`, Domain 미호출 |
| IT-FAIL-02 | 두 조합 모두 실패 | `UI_DOMAIN_FAILURE` |
| IT-FAIL-03 | 저장소 write 실패 | `UI_DATA_FAILURE` |
| IT-FAIL-04 | 손상 데이터 load | `DATA_FORMAT_INVALID` 전파 |
| IT-FAIL-05 | 중복 입력 | `UI_DUPLICATE_NONZERO` |

## 4.3 회귀 보호 규칙

| 규칙 ID | 정책 | 검증 방법 |
|---------|------|-----------|
| RG-01 | 기존 TC ID 삭제로 커버리지 감소 금지 | 리뷰 체크리스트 |
| RG-02 | `int[6]`·필드 순서 변경 금지 | 계약 테스트 |
| RG-03 | Error code·message 고정값 변경 금지 | 골든/스냅샷 |
| RG-04 | 1-index 좌표 규칙 변경 금지 | 경계 단언 |
| RG-05 | Invariant 완화 금지 | INV 스위트 전체 실행 |

### 변경 금지(계약)

- 입력 계약(IC-01~04) 변경 시 전체 테스트 실패 필요.
- 출력 계약(OC-01~09) 변경 시 동일.
- 고정 메시지 변경 시 문자열 테스트 실패 필요.

## 4.4 커버리지 목표

| 영역 | 목표 |
|------|------|
| Domain Logic | **≥ 95%** |
| UI Boundary | **≥ 85%** |
| Data Layer | **≥ 80%** |

**측정**: 라인·브랜치 커버리지 리포트 산출; 정상·실패 경로 모두 포함.

## 4.5 Traceability Matrix (필수)

| Concept(Invariant) | Rule | Use Case | Contract | Test | Component |
|--------------------|------|----------|----------|------|-----------|
| INV-01 | 4×4 고정 | UC-D-01, UC-D-03 | Input schema | D-RED-02, UI-RED-01, IT-FAIL-01 | InputValidator, Boundary |
| INV-02 | 빈칸 2개 | UC-D-01 | Input schema | D-RED-03, UI-RED-02 | InputValidator |
| INV-03 | 0 또는 1~16 | UC-D-03 | Input schema | D-RED-04, UI-RED-03 | InputValidator |
| INV-04 | 0 제외 유일 | UC-D-02 | Input schema | D-RED-05, UI-RED-04, IT-FAIL-05 | InputValidator |
| INV-05 | 누락 2수 | UC-D-02 | Domain API | D-RED-06 | MissingNumbers, FillStrategy |
| INV-06 / MC | 합 34 | UC-D-03, UC-D-04 | solve 계약 | D-RED-07, D-RED-08, IT-OK-02 | MagicSquareJudge, FillStrategy |
| 출력 int[6] | OC-01~04 | UC-D-05 | Output schema | UI-RED-05, UI-RED-07, RG-02 | Boundary Formatter |
| 저장 불변 | 4×4 / 길이 6 | save/load | Repository | DATA-06, DATA-07, IT-FAIL-04 | Repository 구현체 |

---

## 문서 준수 체크리스트

- [ ] 모호어(예: “적절히”) 미사용.
- [ ] 규칙마다 테스트 ID 또는 검증 방법 명시.
- [ ] 구현 코드 없음(표·계약·시나리오만).
- [ ] UI=Boundary, Data=포트 수준 준수.
