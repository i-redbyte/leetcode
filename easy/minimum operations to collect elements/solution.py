from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        result = 0
        mask = (1 << k) - 1
        for i, n in enumerate(reversed(nums), 1):
            if n <= k:
                result |= 1 << (n - 1)
                if result == mask:
                    return i
        return -1

    def minOperations1(self, nums: List[int], k: int) -> int:
        s = set()
        result = 1
        for i in range(1, k + 1):
            s.add(i)
        n = len(nums) - 1
        for i in range(n, 0, -1):
            if nums[i] in s:
                s.remove(nums[i])
            if len(s) == 0:
                return result
            result += 1
        return result


s = Solution()
print(s.minOperations(nums=[3, 1, 5, 4, 2], k=2))
print(s.minOperations(nums=[3, 1, 5, 4, 2], k=5))
print(s.minOperations(nums=[3, 2, 5, 3, 1], k=3))
