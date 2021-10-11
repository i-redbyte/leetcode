class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        list_s1, list_s2 = [], []
        for l1, l2 in zip(s1, s2):
            if l1 == l2:
                continue
            else:
                list_s1.append(l1)
                list_s2.append(l2)
            if len(list_s1) > 2:
                return False
        return list_s1 == list_s2[::-1]

    def areAlmostEqual1(self, s1: str, s2: str) -> bool:
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
print(s.areAlmostEqual("abca", "abcc"))
