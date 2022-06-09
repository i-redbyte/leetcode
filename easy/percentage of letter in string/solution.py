class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        result = 0
        n = len(s)
        for c in s:
            if c == letter:
                result += 1
        return int((result / n) * 100)


s = Solution()
print(s.percentageLetter(s="foobar", letter="o"))
print(s.percentageLetter(s="jjjj", letter="k"))
print(s.percentageLetter(s="jjjj", letter="j"))
print(s.percentageLetter(s="Lenin", letter="L"))
