from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def sieve_of_eratosthenes(n: int) -> List[int]:
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False
            for i in range(2, int(n ** 0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, n + 1, i):
                        is_prime[j] = False
            return [i for i in range(left, n + 1) if is_prime[i]]

        primes_in_range = sieve_of_eratosthenes(right)
        primes_in_range = [p for p in primes_in_range if p >= left]
        if len(primes_in_range) < 2:
            return [-1, -1]
        min_diff = float('inf')
        result = [-1, -1]
        n = len(primes_in_range) - 1
        for i in range(n):
            diff = primes_in_range[i + 1] - primes_in_range[i]
            if diff < min_diff:
                min_diff = diff
                result = [primes_in_range[i], primes_in_range[i + 1]]

        return result


s = Solution()
print(s.closestPrimes(left=10, right=19))
print(s.closestPrimes(left=4, right=6))
