from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        for i in range(n):
            if i == index[i]:
                result[index[i]] = nums[i]
            else:
                for j in range(index[i], i + 1):
                    tmp = result[j]
                    result[j] = nums[i]
                    nums[i] = tmp
        return result


s = Solution()
print(s.createTargetArray(nums=[0, 1, 2, 3, 4], index=[0, 1, 2, 2, 1]))
print(s.createTargetArray(nums=[1, 2, 3, 4, 0], index=[0, 1, 2, 3, 0]))
print(s.createTargetArray(nums=[1], index=[0]))
