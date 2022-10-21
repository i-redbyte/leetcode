from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def getBitMask(i: int) -> int:
            mask = 0
            for w in words[i]:
                mask |= 1 << (ord(w) - ord('a'))
            return mask

        result = 0
        n = len(words)
        masks = [getBitMask(i) for i in range(n)]
        sizes = [len(word) for word in words]

        for i in range(n):
            for j in range(i + 1, n):
                if masks[i] & masks[j] == 0:
                    result = max(result, sizes[i] * sizes[j])
        return result


s = Solution()
print(s.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
print(s.maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]))
print(s.maxProduct(["a", "aa", "aaa", "aaaa"]))
