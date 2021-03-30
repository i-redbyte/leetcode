from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_len = len(min(strs, key=len))
        low, high = 1, min_len
        while low <= high:
            mid = (low + high) // 2
            if self.is_prefix(strs, mid):
                low = mid + 1
            else:
                high = mid - 1
        return strs[0][:high]

    @staticmethod
    def is_prefix(strs, length):
        s = strs[0][:length]
        for i in range(1, len(strs)):
            if not strs[i].startswith(s):
                return False
        return True


s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
print(s.longestCommonPrefix(["dog", "racecar", "car"]))
print(s.longestCommonPrefix(["aaaaaaaa", "aaalin", "aaaas"]))
print(s.longestCommonPrefix(["aaaaaaaa", "alin", "aaaas"]))
print(s.longestCommonPrefix(["bbob", "b", "aaaas"]))
print(s.longestCommonPrefix([]))
print(s.longestCommonPrefix(["11111"]))
