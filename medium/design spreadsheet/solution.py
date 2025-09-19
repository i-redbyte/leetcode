from typing import List


class Spreadsheet:
    def __init__(self, rows: int):
        self.rows = rows
        self.cols = 26
        self.grid: List[List[int]] = [[0] * self.cols for _ in range(rows)]

    def _parse_cell(self, cell: str) -> tuple[int, int]:
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:]) - 1
        return row, col

    def _value_of(self, token: str) -> int:
        token = token.strip()
        if token and token[0].isdigit():
            return int(token)
        r, c = self._parse_cell(token)
        return self.grid[r][c]

    def setCell(self, cell: str, value: int) -> None:
        r, c = self._parse_cell(cell)
        self.grid[r][c] = value

    def resetCell(self, cell: str) -> None:
        r, c = self._parse_cell(cell)
        self.grid[r][c] = 0

    def getValue(self, formula: str) -> int:
        assert formula.startswith("=")
        body = formula[1:].strip()
        x, y = map(str.strip, body.split("+", 1))
        return self._value_of(x) + self._value_of(y)
