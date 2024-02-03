from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]


s = Solution()
print(s.findDifference(nums1=[1, 2, 3], nums2=[2, 4, 6]))
print(s.findDifference(nums1=[1, 2, 3, 3], nums2=[1, 1, 2, 2]))
