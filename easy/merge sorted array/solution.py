from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        k = m + n - 1
        i = m - 1
        j = n - 1
        while i >= 0 or j >= 0:
            if i >= 0 and j >= 0 and nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            elif i >= 0 and j >= 0 and nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            elif j >= 0:
                nums1[k] = nums2[j]
                j -= 1
            else:
                i -= 1
            k -= 1
        """
        Do not return anything, modify nums1 in-place instead.
        """


s = Solution()
s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
s.merge([1], 1, [], 0)
s.merge([0], 0, [1], 1)
