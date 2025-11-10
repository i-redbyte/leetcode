from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        result = 0
        stack = [0]
        for num in nums:
            while stack and stack[-1] > num:
                stack.pop()
            if not stack or stack[-1] < num:
                result += 1
                stack.append(num)
        return result


s = Solution()
print(s.minOperations([0, 2]))
print(s.minOperations([3, 1, 2, 1]))
print(s.minOperations([1, 2, 1, 2, 1, 2]))
