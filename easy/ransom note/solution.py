from collections import Counter


class Solution:
    def canConstruct1(self, ransomNote: str, magazine: str) -> bool:
        s = Counter(ransomNote)
        m = Counter(magazine)
        for ch in s:
            if s[ch] > m[ch] or m[ch] == 0:
                return False
        return True

    # slow
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not Counter(ransomNote) - Counter(magazine)


s = Solution()
print(s.canConstruct(ransomNote="a", magazine="b"))
print(s.canConstruct(ransomNote="aa", magazine="ab"))
print(s.canConstruct(ransomNote="aa", magazine="aab"))
