from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = []
        last = 1 << n
        for i in range(last):
            result.append(i ^ (i >> 1))
        return result


s = Solution()
print(s.grayCode(2))
print(s.grayCode(1))
