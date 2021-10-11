class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        count = 0
        n = len(s1)
        for i in range(n):
            if s1[i] not in s2:
                return False
            if s1[i] != s2[i]:
                count += 1
        return count == 2


s = Solution()
print(s.areAlmostEqual("bank", "kanb"))
print(s.areAlmostEqual("attack", "defend"))
print(s.areAlmostEqual("kelb", "kelb"))
print(s.areAlmostEqual("abcd", "dcba"))
print(s.areAlmostEqual("caa", "aaz"))
