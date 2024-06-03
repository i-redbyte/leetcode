class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_pos, t_pos = 0, 0
        sN = len(s)
        tN = len(t)
        while s_pos < sN and t_pos < tN:
            if s[s_pos] == t[t_pos]:
                t_pos += 1
            s_pos += 1
        return tN - t_pos


s = Solution()
print(s.appendCharacters("coaching", t="coding"))
print(s.appendCharacters("abcde", t="a"))
print(s.appendCharacters("z", t="abcde"))
print(s.appendCharacters("sa", t="z"))
print(s.appendCharacters("abz", t="abc"))
