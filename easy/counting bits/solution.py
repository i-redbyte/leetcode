from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        l = n + 1
        result = [0] * l
        for i in range(1, l):
            result[i] = result[i >> 1] + (i & 1)
        return result

    def countBits1(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            counter = 0
            while i != 0:
                if i & 1 != 0:
                    counter += 1
                i = i >> 1
            result.append(counter)
        return result


s = Solution()
print(s.countBits(2))
print(s.countBits(5))
print(s.countBits(777))
