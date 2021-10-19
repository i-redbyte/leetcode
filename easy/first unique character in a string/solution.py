import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = collections.Counter(s)
        for (i, c) in enumerate(s):
            if counter[c] == 1:
                return i
        return -1

    def firstUniqChar1(self, s: str) -> int:
        d = {}
        control = len(s) + 1
        for (i, c) in enumerate(s):
            if c in d:
                d[c] = control
            else:
                d[c] = i
        result = min(d.values())
        if result == control:
            return -1
        return result


s = Solution()
print(s.firstUniqChar("leetcode"))
print(s.firstUniqChar("loveleetcode"))
print(s.firstUniqChar("aabb"))
