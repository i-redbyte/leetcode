from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0:
            return []
        if n == 1:
            return [str(nums[0])]
        result = []
        current = [nums[0]]
        for i in range(1, n):
            if nums[i] - current[-1] == 1:
                current.append(nums[i])
            else:
                if len(current) > 1:
                    result.append(str(current[0]) + '->' + str(current[-1]))
                    current = [nums[i]]
                else:
                    result.append(str(current[-1]))
                    current = [nums[i]]
            m = len(current)
            if i == n - 1 and m == 1:
                result.append(str(nums[-1]))
            if i == n - 1 and m > 1:
                result.append(str(current[0]) + '->' + str(current[-1]))
        return result


print(Solution().summaryRanges([0, 1, 2, 4, 5, 7]))
print(Solution().summaryRanges([0, 2, 3, 4, 6, 8, 9]))
