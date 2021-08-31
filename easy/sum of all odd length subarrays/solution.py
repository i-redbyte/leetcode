from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0
        i = 1
        j = 0
        n = len(arr)
        while i <= n:
            while j < n and i + j <= n:
                result += sum(arr[j:j + i])
                j += 1
            i += 2
            j ^= j
        return result


s = Solution()

print(s.sumOddLengthSubarrays([1, 4, 2, 5, 3]))
print(s.sumOddLengthSubarrays([1, 2]))
print(s.sumOddLengthSubarrays([10, 11, 12]))
