class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len = 0
        for start in range(n):
            freq = {}
            for end in range(start, n):
                curr_char = s[end]
                freq[curr_char] = freq.get(curr_char, 0) + 1
                counts = set(freq.values())
                if len(counts) == 1:
                    max_len = max(max_len, end - start + 1)
        return max_len


s = Solution()
print(s.longestBalanced("abbac"))
print(s.longestBalanced("zzabccy"))
print(s.longestBalanced("aba"))
