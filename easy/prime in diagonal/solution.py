from math import sqrt
from typing import List


class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def isPrime(n: int) -> bool:
            if n < 2:
                return False
            sq = int(sqrt(n)) + 1
            for i in range(2, sq):
                if n % i == 0:
                    return False
            return True

        result = 0
        n = len(nums)
        for i in range(0, n):
            main_prime = nums[i][i]
            side_prime = nums[i][n - i - 1]
            if isPrime(main_prime):
                if result < main_prime:
                    result = main_prime
            if isPrime(side_prime):
                if result < side_prime:
                    result = side_prime
        return result


s = Solution()
print(s.diagonalPrime([[1, 2, 3], [5, 6, 7], [9, 10, 11]]))
print(s.diagonalPrime([[1, 2, 3], [5, 17, 7], [9, 11, 10]]))
print(s.diagonalPrime([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
