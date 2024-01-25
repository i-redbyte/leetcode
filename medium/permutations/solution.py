from typing import List


class Solution:
    def next_permutation(self, arr: List[int]):
        i = len(arr) - 2
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1
        if i == -1:
            return False
        j = len(arr) - 1
        while arr[j] <= arr[i]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1:] = reversed(arr[i + 1:])
        return True

    def permute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = [nums[:]]
        while self.next_permutation(nums):
            result.append(nums[:])
        return result

    def permute1(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, end):
            if start == end:
                result.append(nums[:])
            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1, end)
                nums[start], nums[i] = nums[i], nums[start]

        result = []
        n = len(nums)
        backtrack(0, n)
        return result


s = Solution()
print(s.permute([1, 2, 3]))
print(s.permute([0, 1]))
print(s.permute([1]))
