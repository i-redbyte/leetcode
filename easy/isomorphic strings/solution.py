class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_t_dic = {}
        t_s_dic = {}
        n = len(s)
        for i in range(n):
            if (s[i] not in s_t_dic) and (t[i] not in t_s_dic):
                s_t_dic[s[i]] = t[i]
                t_s_dic[t[i]] = s[i]
            elif s_t_dic.get(s[i]) != t[i] or t_s_dic.get(t[i]) != s[i]:
                return False
        return True


s = Solution()

print(s.isIsomorphic("egg", "add"))
print(s.isIsomorphic("foo", "bar"))
print(s.isIsomorphic("paper", "title"))
