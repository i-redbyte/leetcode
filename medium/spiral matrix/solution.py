from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        result = []
        n, m = len(matrix), len(matrix[0])
        up, down, left, right = 0, n - 1, 0, m - 1
        s = n * m
        while len(result) < s:
            for col in range(left, right + 1):
                result.append(matrix[up][col])
            for row in range(up + 1, down + 1):
                result.append(matrix[row][right])
            if up != down:
                for col in range(right - 1, left - 1, -1):
                    result.append(matrix[down][col])
            if left != right:
                for row in range(down - 1, up, -1):
                    result.append(matrix[row][left])
            up, down, left, right = up + 1, down - 1, left + 1, right - 1
        return result


s = Solution()
print(s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
