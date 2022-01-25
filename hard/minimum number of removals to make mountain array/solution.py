from typing import List


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        left_stack = []
        right_stack = []

        for i in range(n):
            index = self.find(left_stack, nums[i])
            if index == len(left_stack):
                left_stack.append(nums[i])
            else:
                left_stack[index] = nums[i]
            left[i] = index
            index = self.find(right_stack, nums[n - i - 1])
            if index == len(right_stack):
                right_stack.append(nums[n - i - 1])
            else:
                right_stack[index] = nums[n - i - 1]
            right[n - i - 1] = index

        min_v = len(nums) - 3
        for i in range(n):
            if left[i] >= 1 and right[i] >= 1:
                min_v = min(min_v, n - (left[i] + right[i] + 1))
        # print(left)
        # print(right)
        return min_v

    def find(self, stack: List[int], target: int) -> int:
        left = 0
        right = len(stack)
        while right > left:
            mid = int((right - left) / 2 + left)
            if stack[mid] == target:
                return mid
            elif stack[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left


s = Solution()
print(s.minimumMountainRemovals([1, 3, 1]))
print(s.minimumMountainRemovals([2, 1, 1, 5, 6, 2, 3, 1]))
