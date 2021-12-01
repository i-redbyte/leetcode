from typing import List


class Solution:
    def kmp(self, s) -> List[int]:
        dp = [0]
        j = 0
        for c in s[1:]:
            while j and s[j] != c:
                j = dp[j - 1]

            if s[j] == c:
                j += 1
            dp.append(j)

        return dp

    def maxRepeating(self, sequence: str, word: str) -> int:
        n = len(word)
        max_rep = word * (len(sequence) // n) + ' '
        list = self.kmp(max_rep)
        j = 0
        result = 0
        for c in sequence:
            while j and max_rep[j] != c:
                j = list[j - 1]
            if max_rep[j] == c:
                j += 1
                result = max(result, j // n)
        return result


s = Solution()

print(s.maxRepeating("ababc", "ab"))
print(s.maxRepeating("eeeee", "ab"))
print(s.maxRepeating("eeeee", "e"))
print(s.maxRepeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba", "aaaba"))
