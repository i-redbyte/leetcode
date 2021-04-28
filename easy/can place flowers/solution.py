from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if 0 not in flowerbed:
            return False
        size = len(flowerbed)

        if size < 3 and n == 1:
            return 1 not in flowerbed
        count = 0
        for i in range(0, size):
            current_pos = flowerbed[i]
            if i - 1 >= 0:
                left = flowerbed[i - 1]
            else:
                left = 0
            if i + 1 < size:
                right = flowerbed[i + 1]
            else:
                right = 0
            if current_pos == 0 and left == right == 0:
                flowerbed[i] = 1
                i += 1
                count += 1
        return count >= n


s = Solution()
# print(s.canPlaceFlowers([1, 1, 1, 1, 1], 1))
# print(s.canPlaceFlowers([1, 0, 0, 0, 1], 1))
# print(s.canPlaceFlowers([1, 0, 0, 0, 1], 2))
# print(s.canPlaceFlowers([1, 0, 0, 0, 0, 0, 0], 2))
# print(s.canPlaceFlowers([0, 0, 0, 0, 0], 3))
# print(s.canPlaceFlowers([0, 0], 1))
# print(s.canPlaceFlowers([0, 0, 0], 1))
# print(s.canPlaceFlowers([0, 0, 0], 2))
# print(s.canPlaceFlowers([1, 0, 0, 0, 0, 0, 1], 2))
# print(s.canPlaceFlowers([0, 0, 1, 0, 1], 1))
# print(s.canPlaceFlowers([1, 0, 0, 0, 0, 1], 1))
# print(s.canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2))
# print(s.canPlaceFlowers([1], 0))
print(s.canPlaceFlowers([0, 0, 1, 0, 0], 1))
