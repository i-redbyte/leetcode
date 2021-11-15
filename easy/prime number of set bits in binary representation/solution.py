from math import sqrt


class Solution:
    def isPrime(self, n: int) -> bool:
        if n < 2:
            return False
        sq = int(sqrt(n)) + 1
        for i in range(2, sq):
            if n % i == 0:
                return False
        return True

    def countPrimeSetBits(self, left: int, right: int) -> int:
        result = 0
        right += 1
        for i in range(left, right):
            count = 0
            tmp = i
            while tmp != 0:
                if tmp & 1:
                    count += 1
                tmp = tmp >> 1
            if self.isPrime(count):
                result += 1
        return result


s = Solution()
print(s.countPrimeSetBits(6, 10))
print(s.countPrimeSetBits(10, 15))
