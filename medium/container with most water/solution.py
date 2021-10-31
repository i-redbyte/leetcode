from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        left, right = 0, len(height) - 1

        while left < right:
            min_height = height[right]
            if height[left] < height[right]:
                min_height = height[left]
            current = min_height * (right - left)
            if current > result:
                result = current
            while left < right and height[right] <= min_height:
                right -= 1
            while left < right and height[left] <= min_height:
                left += 1
        return result


s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(s.maxArea([1, 1]))
print(s.maxArea([4, 3, 2, 1, 4]))
print(s.maxArea([1, 2, 1]))
