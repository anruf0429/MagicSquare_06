# 4x4 Magic Square Dual-Track UI + Logic TDD / Clean Architecture 설계 보고서

이 문서는 구현 코드 없이, 레이어 분리 + 계약 기반 테스트 + 리팩토링 안정성을 훈련하기 위한 설계/계약/테스트/통합 계획만 정의한다.

---

# 1) Logic Layer (Domain Layer) 설계

## 1.1 도메인 개념

| 구분 | 이름 | 책임(SRP) | 검증 기준 |
|---|---|---|---|
| Entity | `Matrix4x4` | 4x4 셀 상태 보관 및 좌표 접근 제공 | 행 수=4, 각 행 길이=4 강제 |
| Value Object | `Position` | 1-index 좌표 `(r,c)` 표현 | `r,c ∈ [1,4]` |
| Value Object | `MissingNumbers` | 누락 숫자 2개 표현 | 항상 `small < large` |
| Domain Service | `InputValidator` | 입력 계약 검증(크기, 빈칸, 범위, 중복) | 실패 코드가 규칙별로 1:1 매핑 |
| Domain Service | `MagicSquareJudge` | 마방진 판정(행/열/대각선 합) | 합이 모두 34인지 판정 |
| Domain Service | `FillStrategy` | 두 조합 시도 및 최종 선택 | 반환 순서 규칙 준수 |

## 1.2 도메인 불변조건(Invariants)

| ID | 불변조건 | 검증 규칙 | 실패 코드 |
|---|---|---|---|
| `INV-01` | 행렬 크기 | 행 수=4 AND 각 행 길이=4 | `DOMAIN_INVALID_SIZE` |
| `INV-02` | 빈칸 개수 | 값 `0`의 개수=정확히 2 | `DOMAIN_INVALID_BLANK_COUNT` |
| `INV-03` | 값 범위 | 각 셀은 `0` 또는 `1~16` | `DOMAIN_OUT_OF_RANGE` |
| `INV-04` | 중복 금지 | `0` 제외 값은 중복 없음 | `DOMAIN_DUPLICATE_NONZERO` |
| `INV-05` | 누락 숫자 개수 | `1~16` 중 미등장 숫자=정확히 2 | `DOMAIN_INVALID_MISSING_COUNT` |
| `INV-06` | 마방진 조건 | 모든 행/열/주대각/부대각 합=34 | `DOMAIN_NOT_MAGIC` |

## 1.3 핵심 유스케이스(도메인 관점)

| UC ID | 유스케이스 | 입력 | 출력 | 실패조건 |
|---|---|---|---|---|
| `UC-D-01` | 빈칸 찾기 | `Matrix4x4` | `Position[2]`(row-major) | 빈칸 개수 2가 아님 |
| `UC-D-02` | 누락 숫자 찾기 | `Matrix4x4` | `MissingNumbers{small,large}` | 누락 숫자 개수 2가 아님 |
| `UC-D-03` | 마방진 판정 | `Matrix4x4` | `boolean` | 입력 불변조건 위반 |
| `UC-D-04` | 두 조합 시도 | 행렬 + 빈칸 2개 + 누락숫자 2개 | 성공한 조합 정보 | 두 조합 모두 실패 |
| `UC-D-05` | 출력 포맷 구성 | 성공 조합 정보 | `int[6]` | 길이/순서 규칙 위반 |

## 1.4 Domain API(내부 계약)

> 구현 코드는 제외하고 시그니처/계약만 고정한다.

| API | 입력 | 출력 | 실패조건 |
|---|---|---|---|
| `validateInput(matrix:int[][])` | `4x4 int[][]` | `ValidationResult(ok, errorCode?)` | `INV-01~04` 위반 |
| `findBlankPositions(matrix)` | `Matrix4x4` | `Position[2]` | `INV-02` 위반 |
| `findMissingNumbers(matrix)` | `Matrix4x4` | `MissingNumbers` | `INV-05` 위반 |
| `isMagicSquare(matrix)` | `Matrix4x4` | `boolean` | `INV-01~04` 위반 |
| `solveTwoBlanks(matrix)` | `4x4 int[][]` | `int[6]` | 검증 실패 또는 `INV-06` 위반 |

### 반환 순서 규칙(고정)

- 1차 시도: `(small -> firstBlank, large -> secondBlank)`
- 1차가 마방진이면 해당 순서 반환
- 아니면 2차 시도 `(large -> firstBlank, small -> secondBlank)` 반환
- 반환 형식은 반드시 `[r1,c1,n1,r2,c2,n2]`

## 1.5 Domain 단위 테스트 설계(RED 우선)

| TC ID | 유형 | Given | Expected | 보호 Invariant |
|---|---|---|---|---|
| `D-RED-01` | 정상 | 유효 입력 + 해 존재 | `int[6]` 길이 6, 좌표 1~4 | `INV-01~06` |
| `D-RED-02` | 비정상 | `3x4` 또는 `4x3` | `DOMAIN_INVALID_SIZE` | `INV-01` |
| `D-RED-03` | 비정상 | 빈칸 1개 또는 3개 | `DOMAIN_INVALID_BLANK_COUNT` | `INV-02` |
| `D-RED-04` | 비정상 | 값 `17` 포함 | `DOMAIN_OUT_OF_RANGE` | `INV-03` |
| `D-RED-05` | 비정상 | `0` 제외 중복 존재 | `DOMAIN_DUPLICATE_NONZERO` | `INV-04` |
| `D-RED-06` | 엣지 | 누락 숫자 2개가 아님 | `DOMAIN_INVALID_MISSING_COUNT` | `INV-05` |
| `D-RED-07` | 엣지 | 두 조합 모두 실패 | `DOMAIN_NOT_MAGIC` | `INV-06` |
| `D-RED-08` | 규칙 | 역조합만 성립 | 역조합 순서로 반환 | `INV-06` + 순서규칙 |

### Domain RED 체크리스트

- [ ] 실패 코드가 규칙별로 고정 문자열인지 검증한다.
- [ ] `Position`이 1-index 기준인지 검증한다.
- [ ] 출력 길이가 항상 6인지 검증한다.
- [ ] 조합 순서 규칙이 테스트로 고정되어 있는지 검증한다.

---

# 2) Screen Layer (UI Layer) 설계 (Boundary Layer)

## 2.1 사용자/호출자 관점 시나리오

1. 호출자가 `matrix`를 전달한다.
2. UI Boundary가 입력 계약을 먼저 검증한다.
3. 계약 위반이면 Domain 호출 없이 Error schema를 반환한다.
4. 계약 통과 시 Domain solve를 호출한다.
5. Domain 성공이면 Output schema로 포맷해 반환한다.
6. Domain/Data 실패면 고정된 Error code/message로 매핑해 반환한다.

## 2.2 UI 계약(외부 계약)

### Input schema

```text
{
  matrix: int[4][4]
}
```

검증 규칙:
- shape는 정확히 4x4
- 값은 정수
- 값 범위는 `0` 또는 `1~16`
- `0` 개수는 정확히 2
- `0` 제외 중복 없음

### Output schema

```text
{
  result: int[6] // [r1,c1,n1,r2,c2,n2]
}
```

검증 규칙:
- 길이 6 고정
- `r1,c1,r2,c2`는 1~4
- `n1,n2`는 누락 숫자 2개

### Error schema

```text
{
  code: string,      // 고정 enum
  message: string,   // 고정 문구
  details?: string[] // 선택
}
```

| Error code | 발생 조건 | 고정 message |
|---|---|---|
| `UI_INVALID_SIZE` | 4x4 아님 | `matrix must be 4x4` |
| `UI_INVALID_BLANK_COUNT` | 빈칸 개수 오류 | `matrix must contain exactly two zeros` |
| `UI_OUT_OF_RANGE` | 범위 위반 | `values must be 0 or in [1,16]` |
| `UI_DUPLICATE_NONZERO` | `0` 제외 중복 | `non-zero values must be unique` |
| `UI_DOMAIN_FAILURE` | 도메인 해 없음/판정 실패 | `no valid magic-square completion found` |
| `UI_DATA_FAILURE` | 데이터 저장/로드 실패 | `data layer operation failed` |

## 2.3 UI 레벨 테스트(Contract-first, RED 우선)

> Domain은 Mock 처리한다.

| TC ID | 입력 | Domain Mock | Expected |
|---|---|---|---|
| `UI-RED-01` | 3x4 | 호출되면 실패 | `UI_INVALID_SIZE` + Domain 미호출 |
| `UI-RED-02` | 빈칸 3개 | 호출되면 실패 | `UI_INVALID_BLANK_COUNT` + Domain 미호출 |
| `UI-RED-03` | 값 18 포함 | 호출되면 실패 | `UI_OUT_OF_RANGE` + Domain 미호출 |
| `UI-RED-04` | 중복 5 포함 | 호출되면 실패 | `UI_DUPLICATE_NONZERO` + Domain 미호출 |
| `UI-RED-05` | 유효 입력 | `int[6]` 반환 | Output schema 적합 |
| `UI-RED-06` | 유효 입력 | Domain exception | `UI_DOMAIN_FAILURE` |
| `UI-RED-07` | 유효 입력 | 성공 반환 | 결과 순서 `[r1,c1,n1,r2,c2,n2]` 검증 |

## 2.4 UX/출력 규칙

| 규칙 ID | 규칙 | 테스트 방식 |
|---|---|---|
| `MSG-01` | message는 고정 문자열과 정확 일치 | 문자열 equality 테스트 |
| `MSG-02` | code는 enum 집합 내 값만 허용 | enum membership 테스트 |
| `MSG-03` | 동일 원인은 항상 동일 code/message | 반복 입력 스냅샷 테스트 |
| `OUT-01` | 성공 응답은 `result` 필드만 반환 | 필드 exact match 테스트 |
| `OUT-02` | 에러 응답은 `code,message` 필수 | schema validator 테스트 |

### UI 품질 체크리스트

- [ ] UI 검증 실패 시 Domain 미호출이 보장된다.
- [ ] 에러 문구가 테스트에서 직접 고정된다.
- [ ] 출력 포맷 위반이 즉시 실패한다.

---

# 3) Data Layer 설계 (Data Layer)

## 3.1 목적 정의

- 목적: 입력/결과를 저장/로드하는 경계를 분리해 테스트 대체 가능성을 확보한다.
- 범위: 인터페이스 수준(`Repository Port`)만 정의한다.
- 비범위: DB, 트랜잭션, 락, 분산 처리.

## 3.2 인터페이스 계약

| 메서드 | 입력 | 출력 | 실패 코드 |
|---|---|---|---|
| `saveInput(runId, matrix)` | `string`, `int[4][4]` | `void` | `DATA_WRITE_FAILED` / `DATA_INVARIANT_VIOLATION` |
| `loadInput(runId)` | `string` | `int[4][4]` | `DATA_NOT_FOUND` / `DATA_FORMAT_INVALID` |
| `saveResult(runId, result)` | `string`, `int[6]` | `void` | `DATA_WRITE_FAILED` / `DATA_INVARIANT_VIOLATION` |
| `loadResult(runId)` | `string` | `int[6]` | `DATA_NOT_FOUND` / `DATA_FORMAT_INVALID` |

저장 대상:
- 필수: 입력 행렬
- 선택: 실행 결과(`int[6]`)

## 3.3 구현 옵션 비교(메모리/파일)

| 옵션 | 설명 | 장점 | 단점 | 추천도 |
|---|---|---|---|---|
| A. InMemory | 프로세스 메모리 기반 저장 | 속도 빠름, 테스트 단순 | 프로세스 종료 시 소실 | **기본 추천** |
| B. File(JSON/CSV) | 파일 시스템 기반 저장 | 재현성 높음, 수동 확인 쉬움 | 파일 없음/권한/파싱 예외 처리 필요 | 대체 구현 |

### 추천안

`InMemory`를 기본 저장소로 채택한다.  
이유: 학습 목표가 알고리즘 최적화가 아니라 레이어 분리/계약 테스트이므로, I/O 복잡도를 낮춰 TDD 루프를 빠르게 유지할 수 있다.

## 3.4 Data 레이어 테스트

| TC ID | 대상 | 시나리오 | Expected |
|---|---|---|---|
| `DATA-01` | InMemory | save 후 동일 runId load | 저장값과 완전 동일 |
| `DATA-02` | InMemory | 없는 runId load | `DATA_NOT_FOUND` |
| `DATA-03` | File(JSON) | 정상 파일 load | `int[4][4]` 반환 |
| `DATA-04` | File(JSON) | 파일 없음 | `DATA_NOT_FOUND` |
| `DATA-05` | File(JSON) | 깨진 JSON | `DATA_FORMAT_INVALID` |
| `DATA-06` | 공통 | 4x4 아닌 matrix save | `DATA_INVARIANT_VIOLATION` |
| `DATA-07` | 공통 | 길이 6 아닌 result save | `DATA_INVARIANT_VIOLATION` |

### Data 체크리스트

- [ ] 저장 시 형식 불변조건(4x4 / int[6])을 강제한다.
- [ ] load 실패 원인을 `NOT_FOUND`와 `FORMAT_INVALID`로 분리한다.
- [ ] 구현 교체(InMemory <-> File) 시 상위 테스트가 동일하게 통과한다.

---

# 4) Integration & Verification (통합 및 검증)

## 4.1 통합 경로 정의

흐름:
- `UI Boundary -> Application(선택) -> Domain -> Data Port`

의존성 방향 규칙:
- UI는 Domain 내부 구현을 직접 참조하지 않는다.
- Domain은 UI/Data 구현체를 참조하지 않는다.
- Data 구현체는 Port 계약만 구현한다.

| 레이어 | 의존 가능 | 의존 금지 |
|---|---|---|
| UI | Application API | Domain 내부 객체 생성/조작 |
| Application | Domain API, Repository Port | File/InMemory 구체 클래스 직접 참조 |
| Domain | Domain 타입 | UI DTO, 파일 I/O |
| Data Impl | Repository Port | UI/Domain 서비스 호출 |

## 4.2 통합 테스트 시나리오

### 정상 시나리오(2개 이상)

| ID | 시나리오 | 검증 포인트 |
|---|---|---|
| `IT-OK-01` | 유효 입력 A 처리 | 성공 응답 `int[6]` + 저장 성공 |
| `IT-OK-02` | 유효 입력 B(역조합만 성립) 처리 | 역조합 순서로 결과 반환 |

### 실패 시나리오(3개 이상)

| ID | 시나리오 | Expected |
|---|---|---|
| `IT-FAIL-01` | 입력 크기 오류 | `UI_INVALID_SIZE`, Domain 미호출 |
| `IT-FAIL-02` | 도메인 해 없음 | `UI_DOMAIN_FAILURE` |
| `IT-FAIL-03` | 저장소 write 실패 | `UI_DATA_FAILURE` |
| `IT-FAIL-04` | 손상된 데이터 load | `DATA_FORMAT_INVALID` 전파 |
| `IT-FAIL-05` | 중복 값 입력 | `UI_DUPLICATE_NONZERO` |

## 4.3 회귀 보호 규칙

| 규칙 ID | 정책 | 자동 검증 |
|---|---|---|
| `RG-01` | 기존 테스트 ID 삭제 금지 | 테스트 목록 비교 |
| `RG-02` | 출력 포맷 `int[6]` 변경 금지 | 계약 스냅샷 |
| `RG-03` | 에러 code/message 변경 금지 | 골든 테스트 |
| `RG-04` | 좌표 1-index 규칙 변경 금지 | 경계값 테스트 |
| `RG-05` | Invariant 약화 금지 | Invariant 스위트 상시 실행 |

## 4.4 커버리지 목표

| 영역 | 목표 |
|---|---|
| Domain Logic | 95%+ |
| UI Boundary | 85%+ |
| Data Layer | 80%+ |

측정 기준:
- 라인 커버리지 + 브랜치 커버리지 병행
- 정상/실패 테스트 모두 포함

## 4.5 Traceability Matrix (필수)

| Concept(Invariant) | Rule | Use Case | Contract | Test | Component |
|---|---|---|---|---|---|
| `INV-01` 크기 | 4x4 고정 | `UC-D-01`, `UC-D-03` | Input schema | `D-RED-02`, `UI-RED-01`, `IT-FAIL-01` | `InputValidator`, UI Boundary |
| `INV-02` 빈칸2 | 0 개수=2 | `UC-D-01` | Input schema | `D-RED-03`, `UI-RED-02` | `InputValidator` |
| `INV-03` 범위 | 0 또는 1~16 | `UC-D-03` | Input schema | `D-RED-04`, `UI-RED-03` | `InputValidator` |
| `INV-04` 중복 | 0 제외 유일 | `UC-D-02` | Input schema | `D-RED-05`, `UI-RED-04`, `IT-FAIL-05` | `InputValidator` |
| `INV-05` 누락2 | 미등장 숫자=2 | `UC-D-02` | Domain API | `D-RED-06` | `MissingNumbers`, `FillStrategy` |
| `INV-06` 마방진 | 합=34 | `UC-D-03`, `UC-D-04` | `solveTwoBlanks` | `D-RED-07`, `D-RED-08`, `IT-OK-02` | `MagicSquareJudge`, `FillStrategy` |
| 출력 계약 | `int[6]` 고정 | `UC-D-05` | Output schema | `UI-RED-05`, `UI-RED-07`, `RG-02` | UI Formatter |
| 데이터 불변 | 4x4 / 길이6 유지 | save/load | Repository contract | `DATA-06`, `DATA-07`, `IT-FAIL-04` | Repository 구현체 |

---

## 변경 금지 규칙(최종)

- 입력 계약(4x4, 빈칸 2개, 범위, 중복 금지)은 변경하지 않는다.
- 출력 계약(`int[6]`, 1-index, 순서 규칙)은 변경하지 않는다.
- 에러 code/message 문자열은 테스트 고정값으로 유지한다.
- 위 3개 항목 변경 시 기존 테스트가 실패해야 한다.

