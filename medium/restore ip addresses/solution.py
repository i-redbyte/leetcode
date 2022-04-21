from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def solution(cur, string, length=0):
            if length == 4:
                if len(cur) == len(s) + 3:
                    result.append(cur[:])
                return

            n = len(string)
            for i in range(1, min(n + 1, 4)):
                sub_s = string[0:i]
                len_sub = len(sub_s)
                if 0 <= int(sub_s) < 256 and not (int(sub_s[0]) == 0 and len_sub > 1):
                    if not cur:
                        solution(sub_s, string[i:], length + 1)
                    else:
                        solution(cur + '.' + sub_s, string[i:], length + 1)
        result = []
        solution([], s)
        return result


s = Solution()
print(s.restoreIpAddresses("25525511135"))
print(s.restoreIpAddresses("0000"))
print(s.restoreIpAddresses("101023"))
print(s.restoreIpAddresses("8888"))
