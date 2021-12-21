from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        height = len(matrix)
        width = len(matrix[0])
        dp = [[0] * width for _ in range(height)]
        max_size = 0
        for r in range(height)[::-1]:
            for c in range(width)[::-1]:
                if matrix[r][c] == '0':
                    continue
                dp[r][c] = 1
                if c < width - 1 and r < height - 1:
                    right_size = dp[r][c + 1]
                    corner_size = dp[r + 1][c + 1]
                    down_size = dp[r + 1][c]
                    dp[r][c] = min(1 + right_size, 1 + corner_size, 1 + down_size)
                if dp[r][c] > max_size:
                    max_size = dp[r][c]
        return max_size * max_size


s = Solution()
print(s.maximalSquare(
    [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
print(s.maximalSquare([["0", "1"], ["1", "0"]]))
print(s.maximalSquare([["0"]]))
