from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []
        nums.sort()
        used: List[bool] = [False] * len(nums)
        self.backtrack(nums, [], used, result)
        return result

    def backtrack(self, nums: List[int], path: List[int], used: List[bool], result: List[List[int]]) -> None:
        if len(path) == len(nums):
            result.append(path.copy())
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue

            used[i] = True
            path.append(nums[i])
            self.backtrack(nums, path, used, result)
            path.pop()
            used[i] = False


s = Solution()
print(s.permuteUnique([1, 1, 2]))
print(s.permuteUnique([1, 2, 3]))
