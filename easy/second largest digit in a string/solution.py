class Solution:
    def secondHighest(self, s: str) -> int:
        digits = []
        for x in s:
            if '0' <= x <= '9':
                digits.append(x)
        digits = list(set(digits))
        if len(digits) < 2:
            return -1
        digits.sort()
        return int(digits[-2])


s = Solution()
print(s.secondHighest("dfa12321afd"))
print(s.secondHighest("abc1111"))
print(s.secondHighest("abc1511"))
