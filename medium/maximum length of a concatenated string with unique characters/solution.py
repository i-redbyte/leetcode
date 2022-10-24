from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        unique = ['']
        result = 0
        for i in range(len(arr)):
            for j in range(len(unique)):
                local = arr[i] + unique[j]
                if len(local) == len(set(local)):
                    unique.append(local)
                    result = max(result, len(local))
        return result


s = Solution()
print(s.maxLength(["un", "iq", "ue"]))
print(s.maxLength(["cha", "r", "act", "ers"]))
print(s.maxLength(["abcdefghijklmnopqrstuvwxyz"]))
