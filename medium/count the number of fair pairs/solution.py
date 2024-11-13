from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def compute(target: int) -> int:
            result = 0
            start = 0
            end = len(nums) - 1
            while start < end:
                if nums[start] + nums[end] <= target:
                    result += (end - start)
                    start += 1
                else:
                    end -= 1
            return result

        nums.sort()
        big_counter = compute(upper)
        small_counter = compute(lower - 1)
        return big_counter - small_counter


s = Solution()
print(s.countFairPairs(nums=[0, 1, 7, 4, 4, 5], lower=3, upper=6))
print(s.countFairPairs(nums=[1, 7, 9, 2, 5], lower=11, upper=11))
