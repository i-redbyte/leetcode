from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        result, imax, tmp = 0, 0, 0
        for i in range(n):
            result = max(result, tmp * nums[i])
            tmp = max(tmp, imax - nums[i])
            imax = max(imax, nums[i])
        return result


s = Solution()
print(s.maximumTripletValue([1, 3]))
print(s.maximumTripletValue([12, 6, 1, 2, 7]))
print(s.maximumTripletValue([1, 10, 3, 4, 19]))
print(s.maximumTripletValue([1, 2, 3]))
