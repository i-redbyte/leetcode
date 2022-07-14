from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
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
