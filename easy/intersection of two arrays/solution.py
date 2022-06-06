from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i in nums1:
            if i not in result and i in nums2:
                result.append(i)
        return result

    def intersection3(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        result = []
        k = 0
        n = len(nums1)
        m = len(nums2)
        for i in range(n):
            for j in range(m):
                if nums1[i] == nums2[j] and not nums1[i] in result:
                    result.append(nums1[i])
                    k += 1
        return result

    def intersection1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))


s = Solution()
print(s.intersection(nums1=[1, 2, 2, 1], nums2=[2, 2]))
print(s.intersection(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
