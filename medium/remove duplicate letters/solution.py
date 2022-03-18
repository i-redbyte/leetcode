class Solution:
    def removeDuplicateLetters(self, s):
        last_index = {}
        n = len(s)
        for i in range(n):
            last_index[s[i]] = i
        alphabet = [0] * 26
        result = []
        for i, ch in enumerate(s):
            if not alphabet[ord(ch) - 97]:
                while result and ch <= result[-1] and last_index[result[-1]] > i:
                    alphabet[ord(result[-1]) - 97] = 0
                    result.pop()
                result.append(ch)
                alphabet[ord(ch) - 97] = 1
        return ''.join(result)


s = Solution()
print(s.removeDuplicateLetters("bcabc"))
print(s.removeDuplicateLetters("cbacdcbc"))
print(s.removeDuplicateLetters("lenin"))
