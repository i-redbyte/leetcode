from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        sort_nums = nums.copy()
        sort_nums.sort()
        n = len(sort_nums)
        d = {}
        for i in range(n):
            d[sort_nums[i]] = d.get(sort_nums[i], i)
        for j in nums:
            result.append(d[j])
        return result


s = Solution()

print(s.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
print(s.smallerNumbersThanCurrent([6, 5, 4, 8]))
print(s.smallerNumbersThanCurrent([7, 7, 7, 7]))
