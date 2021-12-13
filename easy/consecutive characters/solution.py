class Solution:
    def maxPower(self, s: str) -> int:
        counter = 0
        result = 0
        prev = ""
        for c in s:
            if c == prev:
                counter += 1
            else:
                prev = c
                counter = 1
            result = max(result, counter)
        return result


s = Solution()
print(s.maxPower("leetcode"))
print(s.maxPower("abbcccddddeeeeedcba"))
print(s.maxPower("triplepillooooow"))
print(s.maxPower("hooraaaaaaaaaaay"))
print(s.maxPower("tourist"))
