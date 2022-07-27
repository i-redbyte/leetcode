from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return len(max("".join(map(str, nums)).split("0"), key=len))

    def findMaxConsecutiveOnes1(self, nums: List[int]) -> int:
        result = 0
        counter = 0
        for i in nums:
            if i == 1:
                counter += 1
                result = max(counter, result)
            else:
                counter = 0
        return result


s = Solution()
print(s.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
print(s.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))
print(s.findMaxConsecutiveOnes([0, 0]))
print(s.findMaxConsecutiveOnes([0]))
print(s.findMaxConsecutiveOnes([1]))
print(s.findMaxConsecutiveOnes([]))
