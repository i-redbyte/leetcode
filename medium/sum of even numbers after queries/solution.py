from typing import List


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        evenSum = 0
        for _ in nums:
            if not _ & 1:
                evenSum += _
        for val, i in queries:
            num = nums[i]
            evenSum = evenSum - num if not num & 1 else evenSum
            num += val
            nums[i] = num
            evenSum = evenSum + num if not num & 1 else evenSum
            result.append(evenSum)
        return result

    def sumEvenAfterQueries1(self, nums: List[int], queries: List[List[int]]) -> List[int]:
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
