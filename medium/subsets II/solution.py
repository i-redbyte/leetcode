from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
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
