from typing import List


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = 0
        last_used = -9999999999999999999

        for num in nums:
            if last_used < num + k:
                last_used = max(last_used + 1, num - k)
                result += 1

        return result


s = Solution()
print(s.maxDistinctElements(nums=[1, 2, 2, 3, 3, 4], k=2))
print(s.maxDistinctElements(nums=[4, 4, 4, 4], k=1))
