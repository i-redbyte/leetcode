from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        tmp = ""
        for word in words:
            tmp += word
            if s == tmp:
                return True
        return False

    def isPrefixString1(self, s: str, words: List[str]) -> bool:
        pos = 0
        n = len(s)
        for word in words:
            len_word = len(word)
            if pos >= n:
                return True
            if s[pos:len_word + pos] != word:
                return False
            pos += len_word
        return pos >= n


s = Solution()
print(s.isPrefixString("iloveleetcode", ["i", "love", "leetcode", "apples"]))
print(s.isPrefixString("iloveleetcode", ["apples", "i", "love", "leetcode"]))
print(s.isPrefixString("a", ["aa", "aaaa", "banana"]))
print(s.isPrefixString("ccccccccc", ["c", "cc"]))
