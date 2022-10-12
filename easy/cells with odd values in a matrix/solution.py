from typing import List


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        row = []
        col = []
        for indice in indices:
            if indice[0] in row:
                row.remove(indice[0])
            else:
                row.append(indice[0])
            if indice[1] in col:
                col.remove(indice[1])
            else:
                col.append(indice[1])
        col_length = len(col)
        row_length = len(row)
        return col_length * n + row_length * m - 2 * col_length * row_length


s = Solution()
print(s.oddCells(m=2, n=3, indices=[[0, 1], [1, 1]]))
print(s.oddCells(m=2, n=2, indices=[[1, 1], [0, 0]]))
