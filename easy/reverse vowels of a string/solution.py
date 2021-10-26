class Solution:
    def reverseVowels(self, s: str) -> str:  # Time Limit Exceeded solution
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        d = dict()
        for (i, ch) in enumerate(s):
            if ch in vowels:
                d[i] = ch
        n = len(d) + 1
        result = list(s)
        for i in range(1, n):
            key_last = sorted(d.keys())[-i]
            key_first = sorted(d.keys())[i - 1]
            result[key_first] = d[key_last]
        return ''.join(result)


s = Solution()
print(s.reverseVowels("hello"))
print(s.reverseVowels("leetcode"))
