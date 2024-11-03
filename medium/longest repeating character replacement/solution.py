from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = defaultdict(int)
        left = 0
        max_count = 0
        result = 0
        for right in range(len(s)):
            char_count[s[right]] += 1
            max_count = max(max_count, char_count[s[right]])
            if (right - left + 1) - max_count > k:
                char_count[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)

        return result


s = Solution()
print(s.characterReplacement(s="ABAB", k=2))
print(s.characterReplacement(s="AABABBA", k=1))
