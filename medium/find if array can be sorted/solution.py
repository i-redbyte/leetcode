from typing import List


class Solution:

    def count_bits(self, num):
        return bin(num).count('1')

    def canSortArray(self, nums: List[int]) -> bool:
        maxx = float('-inf')
        curr_max = nums[0]
        curr_min = nums[0]
        set_bits = self.count_bits(nums[0])

        for i in range(1, len(nums)):
            if set_bits == self.count_bits(nums[i]):
                curr_max = max(curr_max, nums[i])
                curr_min = min(curr_min, nums[i])
            else:
                if curr_min < maxx:
                    return False

                maxx = curr_max
                set_bits = self.count_bits(nums[i])
                curr_min = nums[i]
                curr_max = nums[i]

        return curr_min > maxx


s = Solution()
print(s.canSortArray([8, 4, 2, 30, 15]))
print(s.canSortArray([1, 2, 3, 4, 5]))
print(s.canSortArray([3, 16, 8, 4, 2]))
