from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        n = len(arr) - 1
        while i < n:
            if arr[i] == 0:
                arr.insert(i + 1, 0)
                i += 1
                arr.pop()
            i += 1


s = Solution()
s.duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0])
s.duplicateZeros([1, 2, 3])
