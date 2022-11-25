class Solution:
    def numberOfMatches(self, n: int) -> int:
        result = 0
        advance = n
        while advance != 1:
            matches = advance // 2
            advance = advance - (advance // 2)
            result += matches
        return result


s = Solution()
print(s.numberOfMatches(7))
print(s.numberOfMatches(14))
