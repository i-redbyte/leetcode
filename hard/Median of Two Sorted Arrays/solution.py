from typing import List


class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def median(x):
            n = len(x)
            if n % 2 == 0:
                median1 = x[n // 2]
                median2 = x[n // 2 - 1]
                med = (median1 + median2) / 2
            else:
                med = x[n // 2]
            return med

        if not nums1:
            return median(nums2)
        elif not nums2:
            return median(nums1)
        else:
            if not all(nums1) and not all(nums2):
                return 0.00000
            else:
                nums1.extend(nums2)
                nums1.sort()
                return median(nums1)


s = Solution()
print(s.findMedianSortedArrays([1, 3], [2]))
print(s.findMedianSortedArrays([1, 2], [3, 4]))
print(s.findMedianSortedArrays([0, 0], [0, 0]))
print(s.findMedianSortedArrays([], [1]))
print(s.findMedianSortedArrays([2], []))
