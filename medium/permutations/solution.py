from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, end):
            if start == end:
                result.append(nums[:])
            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1, end)
                nums[start], nums[i] = nums[i], nums[start]

        result = []
        n = len(nums)
        backtrack(0, n)
        return result


s = Solution()
print(s.permute([1, 2, 3]))
print(s.permute([0, 1]))
print(s.permute([1]))
