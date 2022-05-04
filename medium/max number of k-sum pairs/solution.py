from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        table = {}
        result = 0
        for n in nums:
            current = table.get(k - n, 0)
            if current:
                result += 1
                table[k - n] -= 1
            else:
                table[n] = table.get(n, 0) + 1
        return result


print(Solution().maxOperations(nums=[1, 2, 3, 4], k=5))
print(Solution().maxOperations(nums=[3, 1, 3, 4, 3], k=6))
