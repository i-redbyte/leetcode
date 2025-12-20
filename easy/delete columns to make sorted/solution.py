from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        result = 0
        for col in range(m):
            for row in range(n - 1):
                if strs[row][col] > strs[row + 1][col]:
                    result += 1
                    break

        return result


s = Solution()
print(s.minDeletionSize(["cba", "daf", "ghi"]))
print(s.minDeletionSize(["a", "b"]))
print(s.minDeletionSize(["zyx", "wvu", "tsr"]))
