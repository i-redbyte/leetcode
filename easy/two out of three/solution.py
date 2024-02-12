from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s1, s2, s3 = set(nums1), set(nums2), set(nums3)
        i1 = s1.intersection(s2)
        i2 = s1.intersection(s3)
        i3 = s2.intersection(s3)
        return list(i1.union(i2).union(i3))


s = Solution()
print(s.twoOutOfThree(nums1=[1, 1, 3, 2], nums2=[2, 3], nums3=[3]))
print(s.twoOutOfThree(nums1=[3, 1], nums2=[2, 3], nums3=[1, 2]))
print(s.twoOutOfThree(nums1=[1, 2, 2], nums2=[4, 3, 3], nums3=[5]))
