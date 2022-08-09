from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        numeric_map = [0] * 201
        result = 0
        for i in nums:
            if i >= 2 * diff:
                result += numeric_map[i - diff] and numeric_map[i - 2 * diff]
            numeric_map[i] = 1
        return result


s = Solution()
print(s.arithmeticTriplets(nums=[0, 1, 4, 6, 7, 10], diff=3))
print(s.arithmeticTriplets(nums=[4, 5, 6, 7, 8, 9], diff=2))
