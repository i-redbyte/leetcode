from typing import List


class Solution:
    def getMinutes(self, hh: str, mm: str) -> int:
        h = int(hh)
        m = int(mm)
        return (h * 60) + m

    def findMinDifference(self, timePoints: List[str]) -> int:
        t = sorted(int(t[:2]) * 60 + int(t[-2:]) for t in timePoints)
        t.append(t[0] + 1440)
        return min(b - a for a, b in zip(t, t[1:]))

    def findMinDifference1(self, timePoints: List[str]) -> int:
        if len(timePoints) < 2:
            return 0
        minutes = []
        for t in timePoints:
            item = t.split(":")
            minutes.append(self.getMinutes(item[0], item[1]))
        minutes.sort()
        minutes.append(minutes[0] + 1440)
        n = len(minutes)
        result = 99999999
        for i in range(1, n):
            result = min(result, minutes[i] - minutes[i - 1])
        return result


s = Solution()
print(s.findMinDifference(["23:59", "00:00"]))
print(s.findMinDifference(["00:00", "23:59", "00:00"]))
print(s.findMinDifference(["12:12", "00:13"]))
print(s.findMinDifference(["01:01", "02:01", "03:00"]))
