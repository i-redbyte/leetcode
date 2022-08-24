from typing import List


class Solution:
    def recPass(self, nums, result, tmp, start):
        result.append(tmp)
        n = len(nums)
        for i in range(start, n):
            if not (i > start and nums[i - 1] == nums[i]):
                self.recPass(nums, result, tmp + [nums[i]], i + 1)

    def subsetsWithDup(self, nums):
        nums.sort()
        result = []
        self.recPass(nums, result, [], 0)
        return result

    def subsetsWithDup1(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        n2 = 2 ** n
        for i in range(n2):
            tmp = []
            for j in range(n):
                if i & (1 << j) == 0:
                    tmp.append(nums[j])
            if tmp not in result:
                result.append(tmp)
        return result


print(Solution().subsetsWithDup([1, 2, 2]))
print(Solution().subsetsWithDup([0]))
