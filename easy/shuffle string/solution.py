from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [""] * len(s)
        for i, j in enumerate(indices):
            result[j] = s[i]
        return "".join(result)


s = Solution()
print(s.restoreString(s="codeleet", indices=[4, 5, 6, 7, 0, 2, 1, 3]))
