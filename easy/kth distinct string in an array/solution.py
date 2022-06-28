from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        uniq = []
        n = len(arr)
        if n == 1:
            return arr[0]
        for i in range(n):
            if arr[i] not in arr[i + 1:] and arr[i] not in arr[:i]:
                uniq.append(arr[i])
        if k > n or k > len(uniq):
            return ""
        return uniq[k - 1]


s = Solution()

print(s.kthDistinct(arr=["d", "b", "c", "b", "c", "a"], k=2))
print(s.kthDistinct(["aaa", "aa", "a"], k=1))
print(s.kthDistinct(arr=["a", "b", "a"], k=3))
print(s.kthDistinct(arr=["dbty"], k=1))
print(s.kthDistinct(arr=["dbty", "dbty"], k=1))
print(s.kthDistinct(arr=["uyvp", "vufb", "ml", "uc", "pr", "sit", "xx"], k=7))
