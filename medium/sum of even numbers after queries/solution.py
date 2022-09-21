from typing import List


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        s = sum(x for x in nums if x % 2 == 0)
        result = []
        for x, i in queries:
            if nums[i] % 2 == 0:
                s -= nums[i]
            nums[i] += x
            if nums[i] % 2 == 0:
                s += nums[i]
            result.append(s)
        return result


s = Solution()
print(s.sumEvenAfterQueries(nums=[1, 2, 3, 4], queries=[[1, 0], [-3, 1], [-4, 0], [2, 3]]))
print(s.sumEvenAfterQueries(nums=[1], queries=[[4, 0]]))
