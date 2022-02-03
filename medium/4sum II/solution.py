from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        kit = {}
        result = 0
        for i in nums1:
            for j in nums2:
                adder = i + j
                if adder not in kit:
                    kit[adder] = 0
                kit[adder] += 1
        for i in nums3:
            for j in nums4:
                adder = i + j
                if -adder in kit:
                    result += kit[-adder]
        return result


s = Solution()
print(s.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))
print(s.fourSumCount([0], [0], [0], [0]))
