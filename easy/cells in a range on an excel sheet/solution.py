from typing import List


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        result = []
        k1 = s[:1]
        v1 = s[1:2]
        k2 = s[3:4]
        v2 = s[4:]
        start = ord(k1)
        stop = ord(k2) + 1
        begin = int(v1)
        end = int(v2) + 1
        for i in range(start, stop):
            x = chr(i)
            for j in range(begin, end):
                y = x + str(j)
                result.append(y)
        return result


s = Solution()
print(s.cellsInRange("K1:L2"))
print(s.cellsInRange("A1:F1"))
