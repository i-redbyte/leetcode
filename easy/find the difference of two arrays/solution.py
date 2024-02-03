from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        def binarySearch(arr: List[int], target: int) -> bool:
            low, high = 0, len(arr) - 1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return False

        nums1.sort()
        nums2.sort()
        unique1 = []
        unique2 = []

        n = len(nums1)
        for i in range(n):
            if (i == 0 or nums1[i] != nums1[i - 1]) and not binarySearch(nums2, nums1[i]):
                unique1.append(nums1[i])

        n = len(nums2)
        for i in range(n):
            if (i == 0 or nums2[i] != nums2[i - 1]) and not binarySearch(nums1, nums2[i]):
                unique2.append(nums2[i])

        return [unique1, unique2]

    def findDifference1(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]


s = Solution()
print(s.findDifference(nums1=[1, 2, 3], nums2=[2, 4, 6]))
print(s.findDifference(nums1=[1, 2, 3, 3], nums2=[1, 1, 2, 2]))
