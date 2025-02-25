from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        modulo = 10 ** 9 + 7
        even_count, odd_count = 1, 0
        current_sum = 0
        result = 0

        for num in arr:
            current_sum += num
            if current_sum % 2 == 0:
                result += odd_count
                even_count += 1
            else:
                result += even_count
                odd_count += 1

        return result % modulo


s = Solution()
print(s.numOfSubarrays([1, 3, 5]))
print(s.numOfSubarrays([2, 4, 6]))
print(s.numOfSubarrays([1, 2, 3, 4, 5, 6, 7]))
