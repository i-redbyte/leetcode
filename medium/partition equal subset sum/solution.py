from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        stack = [(0, 0)]
        seen = {}
        all_sum = sum(nums)
        if all_sum % 2 != 0:
            return False
        part_sum = all_sum / 2
        while stack:
            i, tmp = stack.pop()
            if tmp == part_sum:
                return True
            elif tmp > part_sum:
                continue
            elif i >= len(nums):
                continue
            elif tmp < part_sum and (i, tmp) not in seen:
                seen[(i, tmp)] = True
                stack.append((i + 1, tmp))
                stack.append((i + 1, tmp + nums[i]))
        return False


s = Solution()
print(s.canPartition([1, 5, 11, 5]))
print(s.canPartition([1, 2, 3, 5]))
