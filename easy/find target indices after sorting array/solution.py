from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        result = []
        first = self.entry_start(nums, target, True)
        end = self.entry_start(nums, target, False)
        if first == -1 and end == -1:
            return []
        for i in range(first, end + 1):
            result.append(i)
        return result

    def entry_start(self, nums: List[int], target: int, is_first: bool) -> int:
        result = -1
        nums = sorted(nums)
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                result = mid
                if is_first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return result


s = Solution()
print(s.targetIndices(nums=[1, 2, 5, 2, 3], target=2))
print(s.targetIndices(nums=[1, 2, 5, 2, 3], target=3))
print(s.targetIndices(nums=[1, 2, 5, 2, 3], target=5))
