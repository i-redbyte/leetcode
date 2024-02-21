from typing import List


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        result = []
        while nums:
            m1 = min(nums)
            nums.remove(m1)
            if not nums:
                result.append(m1)
                break
            m2 = min(nums)
            nums.remove(m2)
            result.append(m2)
            result.append(m1)
        return result


s = Solution()
print(s.numberGame([5, 4, 2, 3]))
print(s.numberGame([5, 4, 2, 3, 1]))
print(s.numberGame([2, 5]))
print(s.numberGame([1, 2, 3]))
print(s.numberGame([]))
print(s.numberGame([8]))
