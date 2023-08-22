from typing import List


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        n = len(hours)
        result = 0
        for i in range(n):
            if target <= hours[i]:
                result += 1
        return result

    def numberOfEmployeesWhoMetTarget1(self, hours: List[int], target: int) -> int:
        n = len(hours) - 1
        half = n // 2
        i = 0
        result = 0
        while i <= half:
            if hours[n - i] >= target:
                result += 1
            if hours[i] >= target and i != n - i:
                result += 1
            i += 1
        return result


s = Solution()
print(s.numberOfEmployeesWhoMetTarget(hours=[0, 1, 2, 3, 4], target=2))
print(s.numberOfEmployeesWhoMetTarget(hours=[5, 1, 4, 2, 2], target=6))
