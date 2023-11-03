from typing import List


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
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
