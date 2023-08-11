class Solution:
    def pivotInteger(self, n: int) -> int:
        sum = ((1 + n) * n) // 2
        s1 = 0
        for i in range(1, n + 1):
            s1 += i
            s2 = i + sum - s1
            if s1 == s2:
                return i
        return -1


s = Solution()
print(s.pivotInteger(8))
print(s.pivotInteger(1))
print(s.pivotInteger(4))
