from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return arr.index(max(arr))


s = Solution()
print(s.peakIndexInMountainArray([0, 1, 0]))
print(s.peakIndexInMountainArray([0, 2, 1, 0]))
print(s.peakIndexInMountainArray([0, 10, 5, 2]))
print(s.peakIndexInMountainArray([3, 4, 5, 1]))
print(s.peakIndexInMountainArray([24, 69, 100, 99, 79, 78, 67, 36, 26, 19]))
