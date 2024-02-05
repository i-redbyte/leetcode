from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image[0])
        for row in image:
            for i in range(n // 2):
                temp = row[i]
                row[i] = row[n - 1 - i]
                row[n - 1 - i] = temp

            for i in range(n):
                row[i] = 1 - row[i]
        return image

    def flipAndInvertImage1(self, image: List[List[int]]) -> List[List[int]]:
        return [[1 ^ i for i in row[::-1]] for row in image]


s = Solution()
print(s.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
print(s.flipAndInvertImage([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))
