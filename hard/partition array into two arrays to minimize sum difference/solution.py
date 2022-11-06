from typing import List


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        all_sum = sum(nums)
        n = len(nums)
        if n == 2:
            return abs(nums[0] - nums[1])
        s1 = self.kSum(nums[0:n // 2])
        s2 = self.kSum(nums[n // 2:n])

        target = all_sum / 2
        result = 9999999999999999
        for i in range(n // 2):
            j = n // 2 - i
            y = len(s2[j]) - 1
            for x in s1[i]:
                while y >= 0:
                    result = min(result, abs(all_sum - 2 * (x + s2[j][y])))
                    if s2[j][y] + x > target:
                        y -= 1
                    else:
                        break
        return result

    def kSum(self, nums: List[int]) -> list[list]:
        m = len(nums)
        s = [0] * (m + 1)
        for i in range(m + 1):
            s[i] = set()
        n = 0
        s[0].add(0)
        for i in nums:
            j = n
            while j >= 0:
                for element in s[j]:
                    s[j + 1].add(element + i)
                j -= 1
            n += 1
        for i in range(len(s)):
            s[i] = sorted(list(s[i]))
        return s


s = Solution()

print(s.minimumDifference([3, 9, 7, 3]))
print(s.minimumDifference([-36, 36]))
print(s.minimumDifference([2, -1, 0, 4, -2, -9]))
