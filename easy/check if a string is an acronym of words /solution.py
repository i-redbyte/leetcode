from typing import List


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return ''.join(x[0] for x in words) == s

    def isAcronym2(self, words: List[str], s: str) -> bool:
        j, n = 0, len(s)
        for str in words:
            if j >= n or s[j] != str[0]:
                return False
            j += 1
        return j == n

    def isAcronym1(self, words: List[str], s: str) -> bool:
        n = len(words)
        acronym = ""
        if n != len(s):
            return False
        for w in words:
            acronym += w[0]
        return acronym == s


s = Solution()
print(s.isAcronym(words=["alice", "bob", "charlie"], s="abc"))
print(s.isAcronym(words=["an", "apple"], s="a"))
print(s.isAcronym(words=["never", "gonna", "give", "up", "on", "you"], s="ngguoy"))
