class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        if n == 3:
            return 1
        prime_list = [2, 3]
        sieve_list = [True] * (n + 1)
        for each_number in self.candidate_range(n - 1):
            if sieve_list[each_number]:
                prime_list.append(each_number)
                for multiple in range(each_number * each_number, n + 1, each_number):
                    sieve_list[multiple] = False
        return len(prime_list)

    def candidate_range(self, n):
        current = 5
        inc = 2
        while current < n + 1:
            yield current
            current += inc
            inc ^= 6


s = Solution()
print(s.countPrimes(5))
print(s.countPrimes(7))
# print(s.countPrimes(1))
# print(s.countPrimes(0))
print(s.countPrimes(3))
print(s.countPrimes(2))
print(s.countPrimes(10))
print(s.countPrimes(100))
# print(s.countPrimes(12))
# print(s.countPrimes(10000000))
