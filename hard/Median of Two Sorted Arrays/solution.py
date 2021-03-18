from typing import List


class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = list(set(nums1 + nums2))
        size = len(merged)
        if size % 2 != 0:
            result = merged[int(size / 2)]
        else:
            right = merged[int(size / 2)]
            left = merged[int(size / 2) - 1]
            result = (left + right) / 2
        return float("{:.4f}".format(float(result)))


s = Solution()
print(s.findMedianSortedArrays([1, 3], [2]))
print(s.findMedianSortedArrays([1, 2], [3, 4]))
print(s.findMedianSortedArrays([0, 0], [0, 0]))
print(s.findMedianSortedArrays([], [1]))
print(s.findMedianSortedArrays([2], []))
