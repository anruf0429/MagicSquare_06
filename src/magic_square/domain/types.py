"""Value objects referenced by domain APIs (DESIGN §1.1)."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Position:
    """1-indexed cell in 4×4, DESIGN OC / FR-02."""

    row: int
    col: int


@dataclass(frozen=True)
class MissingNumbers:
    """The two values absent from 1..16 (small ≤ large), FR-03."""

    small: int
    large: int
