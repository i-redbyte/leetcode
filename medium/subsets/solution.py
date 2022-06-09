from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        start = 2 ** n
        end = 2 ** (n + 1)
        for i in range(start, end):
            mask = bin(i)[3:]
            tmp = []
            for j in range(n):
                if mask[j] == '1':
                    tmp.append(nums[j])
            result.append(tmp)
        return result


s = Solution()
print(s.subsets([1, 2, 3]))
print(s.subsets([6, 8]))
print(s.subsets([0]))
print(s.subsets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 255]))
