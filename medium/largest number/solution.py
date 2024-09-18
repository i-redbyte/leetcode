from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_s = list(map(str, nums))
        nums_s.sort(key=lambda sn: sn * 10, reverse=True)
        if nums_s[0] == "0":
            return "0"
        return "".join(nums_s)


s = Solution()

print(s.largestNumber([10, 2]))
print(s.largestNumber([3, 30, 34, 5, 9]))
