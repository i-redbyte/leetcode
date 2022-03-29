from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return True
            elif nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False


print(Solution().search(nums=[2, 5, 6, 0, 0, 1, 2], target=0))
print(Solution().search(nums=[2, 5, 6, 0, 0, 1, 2], target=3))
