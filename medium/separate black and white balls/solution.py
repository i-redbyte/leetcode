class Solution:
    def minimumSteps(self, s: str) -> int:
        whites, result = 0, 0
        for ch in s:
            if ch == '1':
                whites += 1
            elif ch == '0':
                result += whites
        return result


s = Solution()
print(s.minimumSteps("101"))
print(s.minimumSteps("100"))
print(s.minimumSteps("0111"))
