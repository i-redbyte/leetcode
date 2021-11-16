from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        finds = {}
        result = set()

        nums.sort()
        for i, each in enumerate(nums):
            finds[each] = i

        for i, a in enumerate(nums):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            for j, b in enumerate(nums[i + 1:]):
                c = -(a + b)
                if c in finds and finds[c] > i and finds[c] > j + i + 1:
                    result.add((a, b, c))
        return list(result)


s = Solution()

print(s.threeSum([-1, 0, 1, 2, -1, -4]))
print(s.threeSum([]))
print(s.threeSum([0]))
