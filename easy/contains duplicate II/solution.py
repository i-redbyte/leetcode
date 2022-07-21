from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False


s = Solution()

print(s.containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3))
print(s.containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1))
print(s.containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2))
