class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        eq = {}

        def find(ch: str) -> str:
            if ch not in eq:
                eq[ch] = ch
            else:
                if ch != eq[ch]:
                    eq[ch] = find(eq[ch])
            return eq[ch]

        def union(ch1: str, ch2: str):
            x1, x2 = find(ch1), find(ch2)
            if x1 > x2:
                eq[x1] = x2
            else:
                eq[x2] = x1

        for c1, c2 in zip(s1, s2):
            union(c1, c2)
        result = ''
        for c in baseStr:
            result += find(c)
        return result


s = Solution()
print(s.smallestEquivalentString(s1="parker", s2="morris", baseStr="parser"))
print(s.smallestEquivalentString(s1="hello", s2="world", baseStr="hold"))
print(s.smallestEquivalentString(s1="leetcode", s2="programs", baseStr="sourcecode"))
