from collections import Counter
from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        result: List[int] = []

        for i in range(n - k + 1):
            window = nums[i:i + k]
            freq = Counter(window)
            items = sorted(freq.items(), key=lambda item: (-item[1], -item[0]))
            total = 0
            for idx, (val, cnt) in enumerate(items):
                if idx == x:
                    break
                total += val * cnt

            result.append(total)
        return result


s = Solution()
print(s.findXSum( nums = [1,1,2,2,3,4,2,3], k = 6, x = 2))
print(s.findXSum( nums = [3,8,7,8,7,5], k = 2, x = 2))