from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = dict()
        d[0] = -1
        result = 0
        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1
            if count in d:
                result = max(result, i - d[count])
            else:
                d[count] = i
        return result


s = Solution()
print(s.findMaxLength([0, 1]))
print(s.findMaxLength([0, 1, 0]))
