class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        d = dict()
        for (i, ch) in enumerate(s):
            if ch in vowels:
                d[i] = ch
        n = len(d) + 1
        result = list(s)
        sort_keys = sorted(d.keys())
        for i in range(1, n):
            key_last = sort_keys[-i]
            key_first = sort_keys[i - 1]
            result[key_first] = d[key_last]
        return ''.join(result)


s = Solution()
print(s.reverseVowels("hello"))
print(s.reverseVowels("leetcode"))
