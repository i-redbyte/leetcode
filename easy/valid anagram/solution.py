class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = dict.fromkeys(s, 0)
        t_dict = dict.fromkeys(t, 0)
        for i in s:
            s_dict[i] += 1
        for i in t:
            t_dict[i] += 1
        for i in t:
            if not s_dict.get(i):
                return False
            if t_dict[i] != s_dict[i]:
                return False
        return True


s = Solution()

print(s.isAnagram("anagram", "nagaram"))
print(s.isAnagram("rat", "car"))
print(s.isAnagram("азов", "воза"))
print(s.isAnagram("aa", "bb"))
print(s.isAnagram("xaaddy", "xbbccy"))
print(s.isAnagram("acacbac", "bbbbbac"))
