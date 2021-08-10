from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        n = len(t)
        if len(s) == 0:
            return t
        s_dict = dict.fromkeys(s, 0)
        t_dict = dict.fromkeys(t, 0)
        for i in s:
            s_dict[i] += 1
        for i in t:
            t_dict[i] += 1
        for i in t:
            if not s_dict.get(i):
                return i
            if t_dict[i] > s_dict[i]:
                return i
        return ""

    def findTheDifference_cheaters(self, s: str, t: str) -> str:
        return ' '.join(list(Counter(t) - Counter(s)))


s = Solution()
print(s.findTheDifference("abcd", "abcde"))
print(s.findTheDifference("", "y"))
print(s.findTheDifference("a", "aa"))
print(s.findTheDifference("ae", "aea"))
print(s.findTheDifference("bbbb", "bbbbb"))
print(s.findTheDifference("lenin", "ininel"))
print("===== cheats solution =====")
print(s.findTheDifference_cheaters("abcd", "abcde"))
print(s.findTheDifference_cheaters("", "y"))
print(s.findTheDifference_cheaters("a", "aa"))
print(s.findTheDifference_cheaters("ae", "aea"))
print(s.findTheDifference_cheaters("bbbb", "bbbbb"))
print(s.findTheDifference_cheaters("lenin", "ininel"))
