from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        max_pos = 0
        max_value = arr[0]
        for i in range(1, n):
            if max_value < arr[i]:
                max_value = arr[i]
                max_pos = i
        left = 0
        count = 0
        while left + 1 <= max_pos and arr[left] < arr[left + 1]:
            left += 1
            count += 1
        right = n - 1
        if count == 0 or count == n - 1:
            return False
        while (right >= max_pos and right != 0) and arr[right] < arr[right - 1]:
            right -= 1
            count += 1
        return count == n - 1


s = Solution()
print(s.validMountainArray([2, 1]))
print(s.validMountainArray([3, 5, 5]))
print(s.validMountainArray([0, 3, 2, 1]))
print(s.validMountainArray([0, 1, 3, 2, 1]))
print(s.validMountainArray([0, 1, 5, 5, 2, 1]))
