from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        result = []
        for i in range(len(nums)):
            if nums[i][i] == '0':
                result.append('1')
            else:
                result.append('0')
        return ''.join(result)


s = Solution()
print(s.findDifferentBinaryString(["01", "10"]))
print(s.findDifferentBinaryString(["00", "01"]))
print(s.findDifferentBinaryString(["111", "011", "001"]))
