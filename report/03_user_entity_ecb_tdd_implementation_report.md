# MagicSquare User 엔티티 ECB/TDD 구현 보고서

본 문서는 `.cursorrules` 기반 규칙을 적용하여 `User` 엔티티와 엔티티 단위 테스트를 작성한 작업 결과를 정리한다.

---

## 1) 작업 목적

- ECB 아키텍처 기준으로 `entity` 레이어에 `User` 도메인 객체를 정의
- 타입힌트 + Google docstring 규칙을 준수한 Python 코드 작성
- pytest AAA 패턴으로 엔티티 단위 테스트 작성

---

## 2) 적용한 규칙(.cursorrules 반영)

- 아키텍처: `boundary -> control -> entity` 의존 방향 준수
- 엔티티 책임: 순수 도메인 규칙/검증/계산 중심
- 코드 스타일: Python 3.10+, 타입힌트 필수, public 메서드 Google docstring
- 테스트: pytest, AAA(Arrange-Act-Assert), `test_` 네이밍 규칙
- 금지 규칙: `print()` 디버깅 미사용

---

## 3) 생성 파일

### 3.1 엔티티 파일

- `src/entity/models/user.py`

구현 내용:
- `@dataclass(frozen=True)` 기반 `User` 엔티티 정의
- 필드:
  - `user_id: str`
  - `username: str`
  - `email: str`
  - `preferred_square_size: int = 4`
- 도메인 불변식 검증(`__post_init__`):
  - `user_id` 빈 값/공백 금지
  - `username` 빈 값/공백 금지
  - `email` 기본 형식 검증(`local@domain`)
  - `preferred_square_size == 4` 강제(4x4 도메인 규칙 반영)
- 도메인 메서드:
  - `can_request_magic_square(size: int) -> bool`
  - 지원 크기 여부 판단(4만 허용)

### 3.2 테스트 파일

- `tests/entity/test_user.py`

테스트 내용:
- 정상 생성 케이스 검증
- 비정상 입력 예외 검증:
  - 빈/공백 `user_id`
  - 빈/공백 `username`
  - 잘못된 `email` 형식
  - 지원하지 않는 `preferred_square_size`
- 도메인 메서드 검증:
  - `size=4`일 때 `True`
  - 그 외 크기일 때 `False`

---

## 4) TDD 관점 반영

- RED: 엔티티 요구사항을 테스트 시나리오로 먼저 고정
- GREEN: 테스트 통과를 위한 최소한의 도메인 검증/메서드 구현
- REFACTOR: 과도한 추상화 없이 정적 검증 보조 메서드로 가독성 유지

---

## 5) 검증 결과

- 문법 검증:
  - `python -m py_compile src/entity/models/user.py tests/entity/test_user.py`
  - 결과: 통과

- 테스트 실행:
  - `python -m pytest tests/entity/test_user.py -q`
  - 결과: 실패 (`No module named pytest`)
  - 원인: 현재 실행 환경에 pytest 미설치

---

## 6) 산출물 요약

- ECB 원칙을 준수한 `User` 엔티티 1종 작성 완료
- pytest AAA 기반 엔티티 단위 테스트 작성 완료
- 로컬 환경 의존성(pytest) 부재로 실행 검증은 보류, 문법 검증은 완료
