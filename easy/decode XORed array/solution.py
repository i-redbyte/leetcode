from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = [first]
        for i in encoded:
            # first = first ^ i
            result.append(result[-1] ^ i)
        return result


s = Solution()
print(s.decode([1, 2, 3], 1))
print(s.decode([6, 2, 7, 3], 4))
