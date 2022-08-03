from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1 = ""
        s2 = ""
        for i in word1:
            s1 += i
        for i in word2:
            s2 += i
        return s1 == s2


s = Solution()
print(s.arrayStringsAreEqual(word1=["ab", "c"], word2=["a", "bc"]))
print(s.arrayStringsAreEqual(word1=["a", "cb"], word2=["ab", "c"]))
print(s.arrayStringsAreEqual(["abc", "d", "defg"], word2=["abcddefg"]))
