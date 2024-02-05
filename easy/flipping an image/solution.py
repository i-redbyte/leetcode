from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[1 ^ i for i in row[::-1]] for row in image]


s = Solution()
print(s.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
print(s.flipAndInvertImage([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))
