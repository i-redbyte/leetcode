from typing import List


class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftSum = [0] * n
        rightSum = [0] * n
        result = [0] * n
        for i in range(1, n):
            leftSum[i] = leftSum[i - 1] + nums[i - 1]
            rightSum[n - i - 1] = rightSum[n - i] + nums[n - i]
        for i in range(n):
            result[i] = abs(leftSum[i] - rightSum[i])
        return result


s = Solution()
print(s.leftRigthDifference([10, 4, 8, 3]))  # [15,1,11,22]
print(s.leftRigthDifference([1]))            # [0]
