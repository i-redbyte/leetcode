from typing import List


class Solution:
    # Use binary search for optimization
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left = 0
        right = n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def peakIndexInMountainArray2(self, arr: List[int]) -> int:
        n = len(arr) - 1
        for i in range(1, n):
            if arr[i - 1] <= arr[i] >= arr[i + 1]:
                return i
        return -1

    def peakIndexInMountainArray1(self, arr: List[int]) -> int:
        return arr.index(max(arr))


s = Solution()
print(s.peakIndexInMountainArray([0, 1, 0]))
print(s.peakIndexInMountainArray([0, 2, 1, 0]))
print(s.peakIndexInMountainArray([0, 10, 5, 2]))
print(s.peakIndexInMountainArray([3, 4, 5, 1]))
print(s.peakIndexInMountainArray([24, 69, 100, 99, 79, 78, 67, 36, 26, 19]))
