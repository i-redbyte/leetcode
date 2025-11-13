class Solution:
    def maxOperations(self, s: str) -> int:
        result = 0
        ones = 0
        n = len(s)

        for i, ch in enumerate(s):
            if ch == '1':
                ones += 1
            else:
                if i == n - 1 or s[i + 1] == '1':
                    result += ones
        return result


s = Solution()
print(s.maxOperations("1001101"))
print(s.maxOperations("00111"))
