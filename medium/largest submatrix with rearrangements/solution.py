from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        result = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0

            sorted_heights = sorted(heights, reverse=True)

            for j in range(cols):
                result = max(result, sorted_heights[j] * (j + 1))

        return result


s = Solution()
print(s.largestSubmatrix(matrix=[[0, 0, 1], [1, 1, 1], [1, 0, 1]]))
print(s.largestSubmatrix(matrix=[[1, 0, 1, 0, 1]]))
print(s.largestSubmatrix(matrix=[[1, 1, 0], [1, 0, 1]]))
