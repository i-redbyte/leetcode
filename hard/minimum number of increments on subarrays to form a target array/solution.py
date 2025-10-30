from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        if not target:
            return 0
        ops = target[0]
        for i in range(1, len(target)):
            if target[i] > target[i - 1]:
                ops += target[i] - target[i - 1]
        return ops


s = Solution()
print(s.minNumberOperations([1, 2, 3, 2, 1]))
print(s.minNumberOperations([3, 1, 1, 2]))
print(s.minNumberOperations([3, 1, 5, 4, 2]))
