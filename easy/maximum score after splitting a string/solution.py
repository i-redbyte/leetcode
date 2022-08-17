class Solution:
    def maxScore(self, s: str) -> int:
        result = -1
        zeros = 0
        ones = 0
        n = len(s) - 1
        for i, ch in enumerate(s):
            if ch == '1':
                ones += 1
            else:
                zeros += 1
            if i != n:
                result = max(zeros - ones, result)
        return result + ones


print(Solution().maxScore("011101"))
print(Solution().maxScore("00111"))
print(Solution().maxScore("1111"))
print(Solution().maxScore("00"))
