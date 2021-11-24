from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = -99999
        n = len(nums)
        for i in range(n - 2):
            first_point = i + 1
            second_point = n - 1
            while first_point < second_point:
                tmp = nums[i] + nums[first_point] + nums[second_point]
                if result == -99999:
                    result = tmp
                elif abs(target - result) > abs(target - tmp):
                    result = tmp
                if tmp == target:
                    break
                elif tmp < target:
                    first_point += 1
                else:
                    second_point -= 1
        return result


s = Solution()

print(s.threeSumClosest([-1, 2, 1, -4], 1))
print(s.threeSumClosest([0, 0, 0], 1))
