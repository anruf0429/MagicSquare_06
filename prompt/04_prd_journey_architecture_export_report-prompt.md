# Magic square user journey development
_Exported on 4/28/2026 at 08:26:44 GMT+9 from Cursor (3.2.11)_

---

**User**

Magic Square를 위한 사용자 여정 작성 (Epic → User Story → Task)을 하고자 합니다.
먼저, Level 1: Epic (비즈니스 목표): EPIC — Business Goal에 대한 내용을 다음처럼 작성해 주세요.
Epic: “Invariant(불변조건) 기반 사고 훈련 시스템 구축”
목적
4x4 Magic Square 문제를 활용하여:
Invariant 중심 설계 사고 훈련
Dual-Track TDD 적용 훈련
입력/출력 계약 명확화 훈련
설계 → 테스트 → 구현 → 리팩토링 흐름 체화

성공 기준
Domain Logic 95% 이상 테스트 커버리지
입력 검증 100% 계약 테스트 통과
하드코딩 없음
매직 넘버 없음
Invariant → Test 추적 가능

---

**Cursor**

프로젝트 문서 톤 확인 중입니다.



요청하신 **Level 1: Epic (비즈니스 목표)** 를 아래처럼 정리할 수 있습니다. 복사해 `Epic – User Story – Task` 상위에 두면 됩니다.

---

## EPIC — Business Goal

**Epic**  
`Invariant(불변조건) 기반 사고 훈련 시스템 구축`

**목적**  
4×4 Magic Square 문제를 매개로 다음 역량을 체계적으로 훈련한다.

- **Invariant 중심 설계 사고**: 도메인 불변조건을 먼저 정의하고, 그에 맞춰 설계·구현을 이어가는 습관을 익힌다.  
- **Dual-Track TDD 적용**: “테스트와 구현이 동시에 자라는” 이중 궤적(계약/속성 vs 구체 구현)을 실습한다.  
- **입·출력 계약 명확화**: 엔트리/이그릿 API와 경계 조건을 스펙으로 고정해 오해·누락을 줄인다.  
- **설계 → 테스트 → 구현 → 리팩토링 흐름 체화**: 한 사이클을 반복 가능한 워크플로로 몸에 익힌다.

**성공 기준**

- **Domain logic**: **95% 이상** 테스트 커버리지(또는 동등한 “의미 있는” 커버리지 기준) 달성.  
- **입력 검증**: **100%** 계약 테스트(경계·형식·도메인 규칙) 통과.  
- **하드코딩 없음**: “우연히 맞는” 상수/분기에 의존하지 않는다.  
- **매직 넘버 없음**: 의미 있는 이름(상수·Enum·설정)으로 정리한다.  
- **Invariant → Test 추적 가능**: 각 불변조건이 대응 테스트(또는 시나리오)에 **명시적으로 연결**되어 있다(추적성/추첨 가능).

---

이후 **Level 2: User Story**·**Level 3: Task**를 붙일 때는 각 스토리가 이 Epic의 목적·성공 기준 중 어디에 기여하는지 한 줄씩 맞춰 두면 흐름이 잘 맞습니다. 필요하면 “User Story 템플릿”이나 “Task 쪼개기 기준(예: invariant 단위 / 경계 케이스 단위)”도 같은 형식으로 이어서 써 드리겠습니다.

---

**User**

Level 2: User Journey (사용자 여정)를 다음 내용처럼 작성해 주세요.
Persona
소프트웨어 개발 학습자
TDD 훈련 중
Clean Architecture 이해 중

Journey
Step 1 — 문제 인식
“마방진을 구현한다”가 아니라

Step 2 — 계약 정의
입력 스키마 정의
출력 스키마 정의
예외 정책 정의


Step 3 — Domain 분리
BlankFinder
MissingNumberFinder
MagicSquareValidator
Solver

Step 4 — Dual-Track 진행
UI RED / Logic RED 병렬
GREEN 최소 구현
REFACTOR 통합 정리

Step 5 — 회귀 보호
엣지 케이스 추가
입력 오류 케이스 추가
조합 실패 케이스 추가


---

**Cursor**

아래는 **Level 2: User Journey (사용자 여정)** 을 요청하신 뼈대에 맞춰 문장으로 다듬은 버전입니다.

---

## Level 2: User Journey (사용자 여정)

### Persona

| 구분 | 설명 |
|------|------|
| **역할** | 소프트웨어 개발 **학습자** |
| **맥락** | **TDD**를 실습·훈련 중 |
| **배경** | **Clean Architecture**(경계·의존 방향·레이어 책임)를 이해하는 단계 |

---

### Journey

**Step 1 — 문제 인식**  
목표는 “마방진을 **그냥** 구현한다”가 아니라, **무엇이 항상 참이어야 하는지(Invariant)** 와 **바깥과의 약속(계약)** 을 먼저 세우는 일이다. 구현은 그 다음이다.

**Step 2 — 계약 정의**  
경계에서 허용되는 형태와 실패 시 의미를 고정한다.

- **입력 스키마 정의**: 허용 타입·범위·크기(예: 4×4)·빈 칸 표현 등  
- **출력 스키마 정의**: 성공 시 구조(격자·합·검증 결과 등), 부분 성공 여부  
- **예외 정의**: 검증 실패·솔버 불가·모순 입력 등에 대한 정책과 메시지/코드 체계  

**Step 3 — Domain 분리**  
한 덩어리로 넣지 않고, 책임 단위로 나눈다.

- **BlankFinder**: 빈 칸(또는 후보) 탐색  
- **MissingNumberFinder**: 누락 값 추론·계산  
- **MagicSquareValidator**: 행·열·대각선·합 등 **마방진 불변조건** 검증  
- **Solver**: 위 요소를 조합해 유효한 해를 찾거나 불가를 판정  

**Step 4 — Dual-Track 진행**  
UI와 도메인 로직을 **동시에** 짧은 사이클로 밀어 넣는다.

- **RED (병렬)**: **UI RED**와 **Logic RED**를 나란히 둔다(한쪽만 길게 가지 않음).  
- **GREEN**: 각 트랙에서 **최소 구현**으로 테스트를 통과시킨다.  
- **REFACTOR**: 중복·경계·이름을 정리하고 **통합**한다.  

**Step 5 — 회귀 보호**  
리팩토링과 기능 추가 이후에도 깨지지 않도록 방어막을 쌓는다.

- **엣지 케이스 추가**: 경계 크기·극단 입력·거의 완성된 격자 등  
- **입력 오류 케이스 추가**: 스키마 위반·타입 오류·금지 조합  
- **조합 실패 케이스 추가**: Solver·Validator·Finder 간 연계에서 나는 실패(모순·무해·타임아웃 등)  

---

이 문단은 Epic의 “Invariant 중심·Dual-Track TDD·계약 명확화·설계→테스트→구현→리팩토링”과 1:1로 연결되도록 Step 2·4를 두었습니다. 원하시면 같은 톤으로 **Level 3: Task** 예시(스토리별 체크리스트)까지 이어서 써 드리겠습니다.

---

**User**

Level 3: User Stories
Level 3: User Stories를 다음 내용처럼 작성해 주세요. Story 1 — 입력 검증 As a 학습자 I want to 입력이 정확히 4x4인지 검증되길 원한다 So that 잘못된 데이터가 Domain으로 전달되지 않도록 한다

Acceptance Criteria: 4x4가 아니면 예외 빈칸 2개 아니면 예외 중복 숫자 예외 범위 위반 예외

Story 2 — 빈칸 탐색 As a 학습자 I want to 0의 좌표를 정확히 찾고 싶다 So that 조합 시도가 가능하다

Acceptance Criteria: row-major 순서 유지 정확히 2개 반환

Story 3 — 누락 숫자 탐색 Acceptance Criteria: 1~16 중 누락 2개 오름차순 반환

Story 4 — 마방진 판정 Acceptance Criteria: 모든 행 합 동일 모든 열 합 동일 대각선 동일

Story 5 — 두 조합 시도 Acceptance Criteria: small→first blank 시도 실패 시 reverse 정답 배열 길이 6


---

**Cursor**

아래는 **Level 3: User Stories** 를 요청하신 내용에 맞춰 형식을 통일하고, 빠진 **As / I want / So that** 를 Story 3·4·5에 보완한 버전입니다.

---

## Level 3: User Stories

### Story 1 — 입력 검증

**As a** 학습자  
**I want to** 입력이 **정확히 4×4** 인지 검증되길 원한다  
**So that** 잘못된 데이터가 Domain으로 전달되지 않도록 한다  

**Acceptance Criteria**

- 격자가 4×4가 아니면 **예외**를 발생시킨다.  
- 빈 칸이 **정확히 2개**가 아니면 **예외**를 발생시킨다.  
- **중복된 숫자**가 있으면 **예외**를 발생시킨다.  
- 허용 범위(예: 1~16 및 빈 칸 표현 규칙)를 **위반**하면 **예외**를 발생시킨다.  

---

### Story 2 — 빈칸 탐색

**As a** 학습자  
**I want to** **0**으로 표시된 빈 칸의 **좌표를 정확히** 찾고 싶다  
**So that** 이후 **조합 시도**(숫자 배치 탐색)가 가능하다  

**Acceptance Criteria**

- 빈 칸 목록은 **row-major 순서**를 유지한다.  
- 빈 칸은 **정확히 2개**이며, 각각 **(row, col)** 형태로 **2개**를 반환한다.  

---

### Story 3 — 누락 숫자 탐색

**As a** 학습자  
**I want to** 격자에 **나타나지 않은 숫자**를 알고 싶다  
**So that** 빈 칸에 넣을 **후보 집합**을 확정할 수 있다  

**Acceptance Criteria**

- **1~16** 중 격자에 **누락된 숫자가 정확히 2개**임을 반영한다.  
- 누락된 두 숫자를 **오름차순**으로 반환한다.  

---

### Story 4 — 마방진 판정

**As a** 학습자  
**I want to** 주어진 4×4 격자가 **마방진 조건**을 만족하는지 판정하고 싶다  
**So that** 솔버·검증 단계에서 **동일한 규칙**으로 성공/실패를 말할 수 있다  

**Acceptance Criteria**

- **모든 행**의 합이 **서로 동일**하다.  
- **모든 열**의 합이 **서로 동일**하다.  
- **두 대각선**의 합이 위와 **동일**하다.  

---

### Story 5 — 두 조합 시도

**As a** 학습자  
**I want to** 첫 번째 빈 칸에 대해 **두 가지 조합 전략**(순방향·역방향)을 시도하고 싶다  
**So that** 한쪽 시도가 실패해도 **다른 순서**로 정답을 찾을 수 있다  

**Acceptance Criteria**

- **작은 값 → 첫 번째 빈 칸** 순으로 조합을 시도한다(small → first blank).  
- 그 시도가 **실패**하면 **reverse**(역순/역전략) 시도로 넘어간다.  
- 최종 **정답 배열**의 **길이는 6**이다(프로젝트에서 정의한 “정답 표현” 규격과 일치).  

---

Story 5의 **「정답 배열 길이 6」**은 도메인 정의(예: 배치 스텝 6개, 또는 인코딩 길이 6)에 따라 의미가 고정되어야 합니다. 코드/스펙에 다른 길이 규칙이 있으면 그에 맞춰 AC 한 줄만 바꾸면 됩니다.

---

**User**

Level 4:구현 시나리오 - Technical를 다음 내용처럼 작성해 주세요. Feature: 4x4 마방진 완성

불변조건 기반 로직을 검증하기 위해 TDD를 연습하는 개발자로서 부분적으로 채워진 4x4 마방진을 완성하고 싶다

Background: Given 4x4 행렬이 주어지고 And 0은 빈칸을 의미하며 And 정확히 2개의 셀이 0을 포함하고 있고 And 숫자는 1부터 16 사이여야 하며 And 0을 제외한 중복 숫자는 허용되지 않으며 And 4x4의 마방진 상수는 34이다

Scenario: 작은 수 → 큰 수 순서로 마방진이 완성되는 경우 Given 다음과 같은 행렬이 주어졌을 때: | 16 | 2 | 3 | 13 | | 5 | 11 | 10 | 8 | | 9 | 7 | 0 | 12 | | 4 | 14 | 15 | 0 | When 시스템이 빈칸 좌표를 찾고 And 누락된 두 숫자를 찾은 뒤 And 작은 숫자를 첫 번째 빈칸에 배치하고 And 큰 숫자를 두 번째 빈칸에 배치하면 Then 모든 행의 합은 34여야 하고 And 모든 열의 합은 34여야 하며 And 두 대각선의 합도 34여야 하고 And 결과는 길이 6의 배열로 반환되어야 하며 And 반환되는 좌표는 1-index 기준이어야 한다

Scenario: 역순 배치 시 마방진이 완성되는 경우 Given 다음과 같은 행렬이 주어졌을 때: | 16 | 2 | 3 | 13 | | 5 | 11 | 10 | 8 | | 9 | 7 | 0 | 12 | | 4 | 14 | 15 | 0 | When 작은 숫자를 첫 번째 빈칸에 배치했을 때 마방진이 되지 않고 And 큰 숫자를 첫 번째 빈칸에 배치했을 때 마방진이 되면 Then 시스템은 역순 배치 결과를 반환해야 하며 And 최종 행렬은 마방진 상수 34를 만족해야 한다

Scenario: 빈칸 개수가 올바르지 않은 경우 Given 행렬에 빈칸이 1개만 존재할 때 When 유효성 검증을 수행하면 Then 오류가 발생해야 한다

Scenario: 중복 숫자가 존재하는 경우 Given 0을 제외한 중복 숫자가 포함된 행렬일 때 When 유효성 검증을 수행하면 Then 오류가 발생해야 한다

Scenario: 값의 범위를 벗어난 경우 Given 행렬에 16을 초과하는 숫자가 포함되어 있을 때 When 유효성 검증을 수행하면 Then 오류가 발생해야 한다

---

**Cursor**

아래는 **Level 4: 구현 시나리오 — Technical** 을 Gherkin 스타일로 정리하고, 행렬은 표로 읽기 쉽게 맞춘 버전입니다.

---

## Level 4: 구현 시나리오 — Technical

### Feature: 4×4 마방진 완성

**배경 역할**  
불변조건 기반 로직을 검증하기 위해 **TDD**를 연습하는 개발자로서,  
**부분적으로 채워진 4×4 마방진**을 **완성**하고 싶다.

---

### Background

```gherkin
Given 4×4 행렬이 주어진다
And 0은 빈 칸을 의미한다
And 정확히 2개의 셀이 0을 포함한다
And 숫자는 1부터 16 사이여야 한다
And 0을 제외한 중복 숫자는 허용되지 않는다
And 4×4 마방진의 마방진 상수(magic constant)는 34이다
```

---

### 시나리오용 입력 행렬 (공통)

다음 격자는 여러 시나리오에서 **동일한 Given** 으로 사용한다.

|     | c1 | c2 | c3 | c4 |
|-----|----|----|----|-----|
| r1 | 16 | 2 | 3 | 13 |
| r2 | 5 | 11 | 10 | 8 |
| r3 | 9 | 7 | **0** | 12 |
| r4 | 4 | 14 | 15 | **0** |

---

### Scenario: 작은 수 → 큰 수 순서로 마방진이 완성되는 경우

```gherkin
Given 다음과 같은 4×4 행렬이 주어졌을 때
  | 16 | 2  | 3  | 13 |
  | 5  | 11 | 10 | 8  |
  | 9  | 7  | 0  | 12 |
  | 4  | 14 | 15 | 0  |
When 시스템이 빈 칸 좌표를 찾고
And 누락된 두 숫자를 찾은 뒤
And 작은 숫자를 첫 번째 빈 칸에 배치하고
And 큰 숫자를 두 번째 빈 칸에 배치하면
Then 모든 행의 합은 34여야 하고
And 모든 열의 합은 34여야 하며
And 두 대각선의 합도 34여야 하고
And 결과는 길이 6의 배열로 반환되어야 하며
And 반환되는 좌표는 1-index 기준이어야 한다
```

---

### Scenario: 역순 배치 시 마방진이 완성되는 경우

```gherkin
Given 다음과 같은 4×4 행렬이 주어졌을 때
  | 16 | 2  | 3  | 13 |
  | 5  | 11 | 10 | 8  |
  | 9  | 7  | 0  | 12 |
  | 4  | 14 | 15 | 0  |
When 작은 숫자를 첫 번째 빈 칸에 배치했을 때 마방진이 되지 않고
And 큰 숫자를 첫 번째 빈 칸에 배치했을 때 마방진이 되면
Then 시스템은 역순 배치 결과를 반환해야 하며
And 최종 행렬은 마방진 상수 34를 만족해야 한다
```

---

### Scenario: 빈 칸 개수가 올바르지 않은 경우

```gherkin
Given 행렬에 빈 칸이 1개만 존재할 때
When 유효성 검증을 수행하면
Then 오류가 발생해야 한다
```

---

### Scenario: 중복 숫자가 존재하는 경우

```gherkin
Given 0을 제외한 중복 숫자가 포함된 행렬일 때
When 유효성 검증을 수행하면
Then 오류가 발생해야 한다
```

---

### Scenario: 값의 범위를 벗어난 경우

```gherkin
Given 행렬에 16을 초과하는 숫자가 포함되어 있을 때
When 유효성 검증을 수행하면
Then 오류가 발생해야 한다
```

---

### 구현 참고 (스펙 고정)

| 항목 | 내용 |
|------|------|
| **결과 배열 길이** | 6 (좌표·값 등 도메인에서 정한 6필드 포맷과 일치) |
| **좌표 체계** | **1-index** (행·열) |
| **성공 판정** | 행·열·대각선 합이 모두 **34** |

---

이 문서는 Cucumber/Behave 등에 그대로 옮기려면 `Feature` 파일 상단에 `Background` 를 두고, 첫·두 시나리오만 동일 Given 행렬을 쓰면 됩니다. **길이 6 배열의 필드 순서**(예: `[r1,c1, r2,c2, v1, v2]` 등)가 코드에 이미 있으면 시나리오에 한 줄로 명시해 두면 AC가 더 명확해집니다.

---

**User**

Level 5: 시나리오 검증 및 정리를 다음 내용처럼 작성해 주세요.

시나리오 완성도 체크리스트

✅ 4레벨 일관성 확인

Epic → Journey

 x] Epic의 성공 지표가 Journey에 반영됨
 x] Journey의 모든 단계가 Epic 목표 달성에 기여
 x] Pain Points가 명확히 정의됨

Journey → Story

 x] Journey의 각 Stage마다 최소 1개 Story
 x] Story가체적인 기능으로 변환됨
 x] Acceptance Criteria가 측정 가능

Story → Technical

 x] 모든 AC가 Gherkin 시나리오로 변환
 x] Given-When-Then이 명확
 x] 테스트 자동화 가능

✅ Edge Case 커버리지

정상 케이스

 x] Happy Path 시나리오 존재

예외 케이스

 x] 네트워크 오류
 x] 권한 없음
 x] 잘못된 입력
 x] 중복 실행

경계 케이스

 x] 최솟값, 최댓값
 x] 빈 값
 x] 특수 문자

✅ 사용자 중심성

실제 사용자 검증

  ] 현장 엔지니어 1명과 시나리오 리뷰
  ] 관리자 1명과 Journey 검증
  ] 피드백 반영

감정 흐름

 x] 각 Journey Stage마다 감정 표시
 x] 부정 → 긍정 전환 명확

✅ 구현 가능성

기술 검증

 x] QR 스캔 라이브러리 조사 완료
 x] 오프라인 DB 방식 결정
 x] 자동 검증 알고리즘 설계

데이터 요구사항

 x] 필요한 Entity 모두 정의됨 (Mission 2)
 x] API 스펙 초안 작성



---

**Cursor**

아래는 **Level 5: 시나리오 검증 및 정리** 를 요청하신 뼈대에 맞춰 정리한 문서입니다. Magic Square·로컬 도메인 훈련 맥락에 맞게 **해당 없는 항목은 명시**했고, 체크박스는 `- [x]` / `- [ ]` 로 통일했습니다.

---

## Level 5: 시나리오 검증 및 정리

### 시나리오 완성도 체크리스트

#### 4레벨 일관성 확인

**Epic → Journey**

- [x] Epic의 성공 지표가 Journey에 반영됨 (Invariant·Dual-Track TDD·계약·설계→테스트→구현→리팩토링)
- [x] Journey의 각 단계가 Epic 목표 달성에 기여함 (문제 인식 → 계약 → 도메인 분리 → Dual-Track → 회귀 보호)
- [ ] Pain Points가 명확히 정의됨 *(예: “계약 없이 구현부터 함”, “UI만 길게 RED”, “Invariant와 테스트 추적 단절” 등 문서화 필요 시 체크)*

**Journey → Story**

- [x] Journey의 각 Stage마다 최소 1개 Story에 대응 가능 (검증·빈칸·누락 수·판정·조합 시도)
- [x] Story가 구체적인 기능 단위로 변환됨
- [x] Acceptance Criteria가 측정 가능함 (4×4, 빈 칸 2개, 합 34, 배열 길이 6, 1-index 등)

**Story → Technical**

- [x] 주요 AC가 Gherkin 시나리오로 변환됨 *(Level 4 Feature·Background·Scenario)*
- [x] Given–When–Then이 구분 가능함
- [x] 테스트 자동화 가능함 *(동일 전제로 pytest/Behave 등 매핑 가능)*

---

#### Edge Case 커버리지

**정상 케이스**

- [x] Happy Path 시나리오 존재 *(작은 수→큰 수로 완성, 역순 배치로 완성)*

**예외 케이스** *(도메인·로컬 검증 중심)*

- [ ] 네트워크 오류 *(본 프로젝트 범위 밖 / 해당 없음이면 문서에 “N/A”로 고정)*
- [ ] 권한 없음 *(동일 — 로컬 솔버·학습용이면 N/A)*
- [x] 잘못된 입력 *(빈 칸 개수 오류, 중복, 범위 초과 — Level 4 Scenario에 반영)*
- [ ] 중복 실행 *(동시성·멱등이 요구사항에 없으면 N/A 또는 추후)*

**경계 케이스**

- [x] 최솟값·최댓값 *(숫자 1~16, 마방진 상수 34)*
- [ ] 빈 값 *(입력이 `null`/빈 리스트일 때 정책이 스펙에 있으면 별도 시나리오 추가)*
- [ ] 특수 문자 *(격자가 숫자만 허용이면 “비숫자 입력” AC 추가 시 체크)*

---

#### 사용자 중심성

**실제 사용자 검증** *(학습자·코치 관점으로 조정 가능)*

- [ ] 동료 학습자 또는 리뷰어 1명과 시나리오 리뷰
- [ ] 코치·교육 담당 1명과 Journey 검증 *(또는 셀프 리뷰 체크리스트로 대체 시 명시)*
- [ ] 피드백 반영 *(반영 내역을 Level 5 부록에 한 줄 기록)*

**감정 흐름**

- [ ] 각 Journey Stage마다 감정·마찰 포인트 표시 *(선택 — 교육 디자인 시 유용)*
- [ ] 부정 → 긍정 전환이 서술되어 있음 *(예: 계약 확정 후 불안 감소 등 — 미작성 시 미체크)*

---

#### 구현 가능성

**기술 검증** *(Magic Square 맥락에 맞게 수정)*

- [ ] QR 스캔 라이브러리 조사 완료 → **본 도메인에서는 해당 없음** *(대체: 격자 표현·파서 방식 결정)*
- [ ] 오프라인 DB 방식 결정 → **해당 없음** *(대체: 메모리 구조 / 파일 입력 여부 결정)*
- [x] 자동 검증 알고리즘 설계 *(행·열·대각선 합 34, 빈칸·누락 수 — Story 4·검증 로직과 연계)*

**데이터 요구사항**

- [x] 필요한 Entity·도메인 개념이 정의됨 *(User·격자·BlankFinder 등 Journey Step 3과 정합)*
- [ ] API 스펙 초안 작성 *(Boundary 계약이 함수 시그니처·오류 타입 수준으로 고정되었는지에 따라 체크)*

---

### 한 페이지 요약 (트레이스어빌리티)

| 상위 | 하위 | 상태 |
|------|------|------|
| Epic 성공 기준 | Journey Step 2·4·5 | 정합 |
| Journey | User Stories 1–5 | 정합 |
| Story AC | Level 4 Gherkin | 대부분 매핑 *(빈 입력·비숫자는 보강 여지)* |
| 예외·경계 | 네트워크·권한 | 범위 외 또는 미정 |

---

### 권장 후속 조치 (짧게)

1. **Pain Points** 3~5개를 Epic 부록에 한 번에 적고 Level 5 첫 블록을 `[x]` 로 맞춘다.  
2. Edge에서 **N/A** 인 항목은 체크리스트에서 제거하거나 “범위 외” 한 줄로 고정해 혼동을 줄인다.  
3. **빈 입력·비숫자**가 운영 요구사항이면 Story 1 AC + Gherkin Scenario를 한 줄 추가한다.

원하시면 위 체크리스트를 프로젝트 실제 진행도에 맞춰 **전부 [x]가 되도록** 채울 문장(Pain Points·감정 흐름·API 초안 범위)만 따로 써 드리겠습니다.

---

**User**

당신은 시니어 제품/소프트웨어 아키텍트이며 Dual-Track UI + Logic TDD 및 Concept-to-Code Traceability 전문가입니다. PRD 본문 골격은 Report/4를 축으로 하고, Report/1로 문제·동기를 보강하며, 기능·계약·성공 정의는 Report/2, 품질·개발 원칙은 Report/3(및 cursor 규칙) 에서 가져오는 방식으로 다음 내용을 고려해 docs 폴더에 PRD를 작성해 주세요.

프로젝트: Magic Square (4x4) — TDD 연습용 목적:

알고리즘 난이도보다 TDD 훈련이 목적
Invariant 기반 설계/검증 사고를 체득
입력/출력 계약을 명확히 고정
UI/DB/Web 의존성 없이 순수 로직 중심으로 구현 가능하게 PRD 작성
⚠️ 중요 규칙

구현 코드를 작성하지 마십시오.
새로운 기능을 추가하지 마십시오. (요구사항 범위 유지)
모호한 표현(“적절히”, “충분히” 등)을 사용하지 마십시오.
모든 요구사항은 테스트/검증 가능해야 합니다.
Dual-Track(경계/도메인) 분리를 문서 구조에 반영하십시오.
Concept → Rule → Use Case → Contract → Test → Component 추적성을 반드시 포함하십시오.
출력은 구조화된 Markdown으로 작성하십시오.
[입력/출력 계약(고정)]
입력(Input):

4x4 정수 행렬 int[][]
0은 빈칸
빈칸(0)은 정확히 2개
값 범위: 0 또는 1~16
0을 제외한 중복 숫자 금지
첫 번째 빈칸 정의: row-major(행 우선) 스캔 시 먼저 발견되는 0
출력(Output):

int[6]
좌표는 1-index
포맷: [r1, c1, n1, r2, c2, n2]
n1,n2는 누락 숫자 2개
시도 1: 작은 수 → 첫 빈칸, 큰 수 → 둘째 빈칸
마방진이면 그 순서 반환
시도 2: (시도 1 실패 시) 큰 수 → 첫 빈칸, 작은 수 → 둘째 빈칸
마방진이면 역순 반환
두 시도 모두 실패 시 오류 정책에 따라 처리(명시 필수)
마방진 상수(Magic Constant):

n=4 → 34

---

**Cursor**

기존 Report 문서와 프로젝트 구조를 확인한 뒤 `docs` 폴더에 PRD를 작성합니다.



`report/04` 파일은 없어 `report/02`의 통합·검증·추적 메트릭스와 사용자가 고정한 입출력 계약을 PRD 축으로 통합합니다. `docs` 폴더에 PRD를 작성합니다.



`docs` 폴더가 없어 생성했고, 아래 파일에 PRD를 반영했습니다.

**파일:** `c:\DEV\MagicSquare\docs\PRD_magic_square_4x4_tdd.md`

### 요약

- **축:** `report/02`의 도메인·경계 계약·통합 검증·Traceability Matrix를 본문 뼈대로 사용했고, **`report/04`가 없음**을 문서 헤더에서 명시해, 향후 생기면 동기화하도록 했습니다.
- **`report/01`:** §2 문제 정의·Invariant 개념 요약.
- **`report/02`:** §5~7 고정 입출력·솔브 순서·실패 정책·INV·UC·Boundary 요약, §10 매트릭스.
- **`report/03` + `.cursorrules`:** §8 성공 지표·커버리지·ECB·TDD·금지 규칙.

### 사용자가 준 I/O 계약 반영

- `int[][]` 4×4, `0` 빈 칸 2개, 0 또는 1~16, 0 제외 중복 금지.
- 첫 빈 칸 = row-major 첫 `0`.
- 출력 `int[6]` = `[r1,c1,n1,r2,c2,n2]`, 좌표 **1-index**, `n1,n2` = 누락 두 수.
- 시도 1 (small→첫 빈칸, large→둘째) 성공 시 즉시 반환; 실패 시 시도 2 (역배치); 둘 다 실패 시 **`DOMAIN_NOT_MAGIC` / 경계 `UI_DOMAIN_FAILURE`** 및 고정 메시지 (`report/02`와 동일).

### 범위 준수

- **구현 코드 없음**, **요구 범위 밖 기능 추가 없음** (`report/02`에 이미 있는 Data/UI는 **선택 확장·비필수**로만 서술).
- 모호 표현 대신 테이블·ID·검증 방법으로 고정.
- **Dual-Track**(§6), **Concept → Rule → Use Case → Contract → Test → Component**(§10) 포함.

추가로 PRD 버전 번호나 파일명 규칙을 팀 규칙에 맞추고 싶으면 알려 주세요.

---

**User**

아래 구조를 반드시 지켜 PRD를 작성하십시오.

1. Executive Summary
한 문단 요약
프로젝트가 훈련하려는 핵심 역량(불변조건/계약/TDD)
2. Problem Statement (문제 정의)
“마방진을 만든다”가 아니라 “불변조건을 검증 가능한 형태로 완성한다” 관점으로 정의
왜 입력/출력 계약이 핵심인지 설명
3. Target Users
TDD 학습자/리뷰어 관점
사용 목적/사용 환경(콘솔/테스트 실행)
4. Scope
4.1 In-Scope
빈칸 좌표 찾기
누락 숫자 찾기
마방진 판정
두 조합 시도 후 결과 반환
입력 검증(경계 레이어)
4.2 Out-of-Scope
UI 화면 개발
DB 저장/조회
N×N 일반화(기본 PRD 범위 제외, 확장 항목으로만)
마방진 “생성” 알고리즘(완전 생성 문제)
5. Functional Requirements (기능 요구사항)
각 기능마다 아래 템플릿을 반복해서 작성하십시오:

Feature ID
설명(1~2문장)
입력
처리 규칙(불변조건 포함)
출력
승인 기준(AC) — 반드시 테스트 가능 문장으로
관련 오류/예외 정책
필수 기능 목록:

FR-01 입력 검증 (Boundary)
FR-02 빈칸 탐색
FR-03 누락 숫자 탐색
FR-04 마방진 판정
FR-05 해 찾기(solution): 두 조합 시도 및 반환
6. Business Rules (도메인 규칙)
BR-01 ~ 형태로 나열
“항상 참이어야 하는 규칙”으로 서술
예: 중복 금지, 합 규칙, 좌표 인덱스 규칙, row-major 규칙 등
7. Non-Functional Requirements
테스트 커버리지 목표:
Domain Logic 95%+
Boundary Validation 85%+
결정론적 실행(동일 입력 → 동일 출력)
부작용 금지(입력 행렬 변경 정책 명시)
성능 기준(선택): 4x4 기준 즉시 처리(예: 50ms 내)
8. Dual-Track TDD Strategy
8.1 Track A — Boundary(UI) TDD
Contract-first 테스트 항목 목록
실패 정책(예외 타입/메시지 표준)
8.2 Track B — Domain(Logic) TDD
메서드 단위 테스트 목록
불변조건 테스트 목록
8.3 병렬 진행 규칙
UI RED & Logic RED → UI GREEN & Logic GREEN → REFACTOR
“도메인 먼저 다 구현 후 경계 추가” 금지
9. Test Plan (QA)
시나리오 기반 테스트 목록(정상/역순 성공/실패/입력오류)
회귀 테스트 정책
테스트 데이터(대표 4x4 예시 행렬) 포함
Property/Invariant 기반 체크 항목
10. Architecture Overview (High-Level)
레이어 정의:
Boundary Layer(입력검증/출력형식)
Domain Layer(순수 로직)
책임 분리(SRP)와 확장(OCP) 전략
의존성 방향(도메인이 경계를 모르게)
11. Risks & Ambiguities
모호한 부분을 “결정 항목”으로 명시(예: 두 시도 모두 실패 시 정책)
자주 실수하는 포인트(1-index, row-major, 입력 변경 여부 등)
12. Traceability Matrix (필수)
다음 형식으로 표를 제공하십시오: Concept/Invariant → Business Rule → Feature(FR) → Acceptance Criteria → Test Case → Component

출력 요구사항
전체를 Markdown으로 출력
번호/ID 체계 일관성 유지
구현 코드 작성 금지
모든 요구사항은 검증 가능 문장으로

---

**Cursor**

현재 PRD와 계약을 확인한 뒤, 요청한 12개 섹션 구조로 전면 재작성합니다.



요청한 12개 섹션 구조로 PRD를 전면 재작성합니다.



`docs/PRD_magic_square_4x4_tdd.md`를 요청하신 **12개 섹션 구조**로 다시 썼고, 문서 버전을 **2.0**으로 올렸습니다.

### 구성 요약

| 섹션 | 내용 |
|------|------|
| **1** | Executive Summary(한 문단) + 훈련 역량(Invariant·계약·Dual-Track TDD) |
| **2** | Problem Statement — “만든다”가 아니라 “검증 가능한 불변조건으로 완성/판별”, 계약이 핵심인 이유 |
| **3** | Target Users — 학습자·리뷰어, 콘솔/테스트 실행 |
| **4** | Scope — 4.1 In / 4.2 Out(요청한 항목 그대로) |
| **5** | **FR-01~FR-05** 각각 Feature ID, 설명, 입·처리·출, **측정 가능한 AC**, 오류 정책 |
| **6** | **BR-01~BR-18** 서술형 도메인 규칙 |
| **7** | NFR — 커버리지 95%/85%, 결정론, **입력 행렬 비변조**, 50ms 선택 |
| **8** | Dual-Track — 8.1 계약 테스트·실패 표, 8.2 도메인 TC·불변조건 매핑, 8.3 병렬·금지 사항 |
| **9** | Test Plan — 시나리오 ID, 회귀 정책, **데이터셋 A/B**, Property 체크 |
| **10** | Architecture — Boundary / Domain, SRP·OCP, 의존성 방향 |
| **11** | Risks — DEC-01~04 **결정 항목**, 실수 포인트(1-index, row-major, 입력 변경) |
| **12** | **Traceability** — Concept/Invariant → BR → **FR** → **AC** → **Test Case** → **Component** |

구현 코드는 넣지 않았고, ID는 **FR-xx-AC-yy**, **BR-zz**, **UI-RED-** / **D-RED-** / **TP-** 가 서로 맞도록 맞춰 두었습니다. 수정하고 싶은 AC 문장이 있으면 알려 주세요.

---

**User**

프로젝트: Magic Square (4x4) — TDD 연습용 목적: 알고리즘 난이도보다 “레이어 분리 + 계약 기반 테스트 + 리팩토링” 훈련 제약:

구현 코드는 작성하지 마십시오. (설계/계약/테스트/통합 계획만)
UI는 실제 화면이 아니라 “입력/출력 경계(Boundary)”로 정의
Data Layer는 DB가 아니라 “저장/로드 인터페이스(메모리/파일 교체 가능)” 수준만
입력/출력은 명확히 고정
입력 계약:

4x4 int[][] (0은 빈칸)
빈칸은 정확히 2개
값 범위: 0 또는 1~16
0 제외 중복 금지 출력 계약:
int[6]
좌표는 1-index
반환 형식: [r1,c1,n1,r2,c2,n2]
n1,n2는 두 누락 숫자이며, (작은수→첫빈칸, 큰수→둘째빈칸) 조합이 마방진이면 그 순서로, 아니면 반대로
출력 형식 (반드시 이 구조로)
1) Logic Layer (Domain Layer) 설계
1.1 도메인 개념
Entities / Value Objects / Domain Services 목록과 책임(SRP)
1.2 도메인 불변조건(Invariants)
행/열/대각선 합 일치, Magic Constant 등
1.3 핵심 유스케이스(도메인 관점)
빈칸 찾기, 누락 숫자 찾기, 마방진 판정, 두 조합 시도
1.4 Domain API(내부 계약)
메서드 시그니처 수준(코드 X) + 입력/출력/실패조건
1.5 Domain 단위 테스트 설계(RED 우선)
테스트 케이스 목록(정상/비정상/엣지)
각 테스트가 보호하는 invariant 명시
2) Screen Layer (UI Layer) 설계 (Boundary Layer)
2.1 사용자/호출자 관점 시나리오
“행렬 입력 → 검증 → 결과 출력” 흐름
2.2 UI 계약(외부 계약)
Input schema / Output schema / Error schema
2.3 UI 레벨 테스트(Contract-first, RED 우선)
잘못된 크기, 빈칸 개수 오류, 값 범위 오류, 중복 오류, 반환 포맷 검증
Domain은 Mock으로 가정
2.4 UX/출력 규칙
에러 메시지 표준(정확한 문구 규칙까지)
3) Data Layer 설계 (Data Layer)
3.1 목적 정의
“저장/로드”의 필요성과 범위(학습용)
3.2 인터페이스 계약
예: MatrixRepository.save/load (메서드 수준, 코드 X)
저장 대상: 입력 행렬, 실행 결과(선택)
3.3 구현 옵션 비교(메모리/파일)
옵션 A: InMemory / 옵션 B: File(JSON/CSV)
추천안 1개 선택 + 이유
3.4 Data 레이어 테스트
저장/로드 정합성, 예외(파일 없음/형식 오류), 불변조건(4x4 유지)
4) Integration & Verification (통합 및 검증)
4.1 통합 경로 정의
UI → Application(선택) → Domain → Data 흐름(의존성 방향 포함)
4.2 통합 테스트 시나리오
정상 시나리오 2개 이상
실패 시나리오 3개 이상(입력 오류, 도메인 실패, 데이터 실패)
4.3 회귀 보호 규칙
기존 테스트 유지 정책
변경 금지 규칙(계약/출력 포맷)
4.4 커버리지 목표
Domain Logic 95%+
UI Boundary 85%+
Data 80%+
4.5 Traceability Matrix (필수)
Concept(Invariant) → Rule → Use Case → Contract → Test → Component
추가 조건
모호한 표현 금지(“적절히/충분히” 금지)
모든 규칙은 검증 가능해야 함(테스트로 확인 가능)
구현 코드 작성 금지
표/체크리스트를 적극 사용

---

**Cursor**

`report/02`와 현재 PRD와 정합성을 맞춘 설계·계약·테스트·통합 계획 문서를 `docs`에 작성합니다.



요청한 목차와 제약을 반영한 설계·계약·테스트·통합 계획 문서를 새로 작성합니다.



다음 파일에 **설계·계약·테스트·통합 계획만** 담았습니다(구현 코드 없음).

**`c:\DEV\MagicSquare\docs\DESIGN_layered_architecture_tdd_magic_square_4x4.md`**

### 포함 내용

| 섹션 | 요약 |
|------|------|
| **서두** | 목적(TDD·레이어 분리), UI=**Boundary**, Data=**포트(메모리/파일)** |
| **고정 계약** | IC-01~06, OC-01~09, Magic Constant 34, `small`/`large`·시도1/2·실패 코드 |
| **§1 Domain** | Entity/VO/Service 표, INV-01~06+MC, UC-D-01~05, Domain API 표, `solveTwoBlanks` **검증 정책 택1** 명시, D-RED-01~08 + 체크리스트 |
| **§2 Boundary** | 호출 흐름 6단계, Input/Output/Error schema, **고정 message 전부 표기**, UI-RED-01~07, MSG/OUT 규칙 |
| **§3 Data** | 목적·비범위, **`MatrixRunRepository`/`MatrixRepository` 예시** 메서드 표, InMemory vs File 비교, **InMemory 추천 + 이유**, DATA-01~07 + 체크리스트 |
| **§4 통합** | UI→Application→Domain→Data, 의존성 표, IT-OK/IT-FAIL, RG-01~05, 커버리지 95/85/80, **Traceability Matrix** |
| **마지막** | 준수 체크리스트(모호어 금지·검증 가능·코드 없음) |

PRD(`docs/PRD_magic_square_4x4_tdd.md`)와 `report/02`의 코드·메시지·TC ID와 맞추었고, 기존 `report/02`와 역할이 겹치므로 **운영상 하나를 “정본”으로 두고** 나머지는 상호 참조만 걸어 두면 됩니다. PRD 본문에 이 설계서 링크를 넣길 원하면 요청해 주세요.

---

**User**

report  폴더에 지금 작업한 내용을 보고서로 내보내줘

---

**Cursor**

기존 보고서 형식과 `docs` 문서를 확인한 뒤 `report` 폴더에 통합 보고서를 작성합니다.



`report/04` 번호로 기존 보고서와 맞춰 통합 보고서를 작성합니다.



`report` 폴더에 아래 보고서를 추가했습니다.

**파일:** `c:\DEV\MagicSquare\report\04_prd_journey_architecture_export_report.md`

### 구성 요약

| 절 | 내용 |
|----|------|
| **1** | 작업 목적(Epic~Traceability, PRD, Dual-Track, 계약 설계) |
| **2** | 산출물 목록 — `docs/PRD_magic_square_4x4_tdd.md`, `docs/DESIGN_layered_architecture_tdd_magic_square_4x4.md` |
| **3** | 대화에서 정리한 내용 요약(Epic, Journey, Stories 1~5, Gherkin 방향, Level 5) |
| **4** | 입출력·솔브 순서·Magic 34·Dual-Track·Traceability·NFR 요약 |
| **5** | `report/01`~`03`과의 관계 + 본 문서 역할(내보내기·인덱스) |
| **6** | 결론·후속 권장(문서 정본, 스토리 파일 분리 여부, TC 매핑) |
| **부록** | 참조 경로 목록 |

기존 번호 체계에 맞춰 **`04_`** 접두를 사용했습니다. Epic·여정·스토리 전문을 별도 `report` 파일로도 두길 원하면 파일명만 지정해 주시면 됩니다.

