from collections import Counter


class Solution:
    def digitCount(self, num: str) -> bool:
        di = Counter(map(int, num))
        for i, n in enumerate(num):
            if di[i] != int(n):
                return False
        return True


print(Solution().digitCount("1210"))
print(Solution().digitCount("030"))
