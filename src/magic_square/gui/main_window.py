"""PyQt6 screen layer for the magic-square solver."""

from __future__ import annotations

from PyQt6.QtWidgets import (
    QHBoxLayout,
    QGridLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from magic_square.boundary import BoundaryError, solve_matrix
from magic_square.constants import MATRIX_SIZE


class MainWindow(QMainWindow):
    """Simple 4x4 matrix input screen with solve action."""

    _SAMPLE_MATRIX = [
        [16, 0, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [0, 15, 14, 1],
    ]

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Magic Square 4x4")
        self._cells: list[list[QLineEdit]] = []
        self._result_label = QLabel("Result: -")
        self._build_ui()

    def _build_ui(self) -> None:
        root = QWidget()
        layout = QVBoxLayout()

        grid = QGridLayout()
        for row in range(MATRIX_SIZE):
            row_cells: list[QLineEdit] = []
            for col in range(MATRIX_SIZE):
                cell = QLineEdit()
                cell.setPlaceholderText("0")
                cell.setMaxLength(2)
                cell.setFixedWidth(48)
                grid.addWidget(cell, row, col)
                row_cells.append(cell)
            self._cells.append(row_cells)

        sample_button = QPushButton("샘플 채우기")
        sample_button.clicked.connect(self._on_fill_sample_clicked)
        clear_button = QPushButton("초기화")
        clear_button.clicked.connect(self._on_clear_clicked)
        solve_button = QPushButton("풀기")
        solve_button.clicked.connect(self._on_solve_clicked)
        button_row = QHBoxLayout()
        button_row.addWidget(sample_button)
        button_row.addWidget(clear_button)
        button_row.addWidget(solve_button)

        layout.addLayout(grid)
        layout.addLayout(button_row)
        layout.addWidget(self._result_label)
        root.setLayout(layout)
        self.setCentralWidget(root)

    def _read_matrix(self) -> list[list[int]]:
        matrix: list[list[int]] = []
        for row_cells in self._cells:
            row: list[int] = []
            for cell in row_cells:
                raw = cell.text().strip()
                if raw == "":
                    row.append(0)
                    continue
                row.append(int(raw))
            matrix.append(row)
        return matrix

    def _on_solve_clicked(self) -> None:
        try:
            matrix = self._read_matrix()
            solved = solve_matrix(matrix)
            result = solved["result"]
            self._result_label.setText(f"Result: {result}")
        except ValueError:
            QMessageBox.warning(self, "Input Error", "all cells must be integers")
        except BoundaryError as exc:
            QMessageBox.warning(self, exc.code, exc.message)

    def _on_fill_sample_clicked(self) -> None:
        for row_idx, row in enumerate(self._SAMPLE_MATRIX):
            for col_idx, value in enumerate(row):
                text = "" if value == 0 else str(value)
                self._cells[row_idx][col_idx].setText(text)
        self._result_label.setText("Result: -")

    def _on_clear_clicked(self) -> None:
        for row_cells in self._cells:
            for cell in row_cells:
                cell.clear()
        self._result_label.setText("Result: -")
