class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        mismatches = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                mismatches.append(i)
        if not mismatches:
            return True
        if len(mismatches) == 2:
            i, j = mismatches
            if s1[i] == s2[j] and s1[j] == s2[i]:
                return True
        return False

    def areAlmostEqual2(self, s1: str, s2: str) -> bool:
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
