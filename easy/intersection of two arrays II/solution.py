import collections
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = collections.Counter(nums1)
        result = []
        for num in nums2:
            if counts[num] > 0:
                result += num,
                counts[num] -= 1
        return result


s = Solution()
print(s.intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]))
print(s.intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
print(s.intersect(nums1=[1, 1, 1], nums2=[0, 1, 1, 0, 4]))
