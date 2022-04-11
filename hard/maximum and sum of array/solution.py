from typing import List


class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        def dfs(nums, slots) -> int:
            if not nums:
                return 0
            result = 0
            n = len(slots)
            for i in range(1, n):
                if slots[i] > 0:
                    slots[i] -= 1
                    val = (nums[0] & i) + dfs(nums[1:], slots)
                    if val > result:
                        result = val
                    slots[i] += 1
            return result

        slots = [2] * (numSlots + 1)
        return dfs(nums, slots)


print(Solution().maximumANDSum([1, 2, 3, 4, 5, 6], 3))
print(Solution().maximumANDSum([1, 3, 10, 4, 7, 1], 9))
