class Solution:
    def sumOfMultiples(self, n: int) -> int:
        result = 0
        n1 = n // 3
        n2 = n // 5
        n3 = n // 7
        n4 = n // 15
        n5 = n // 21
        n6 = n // 35
        n7 = n // 105
        result += (n1 * (3 + (n - n % 3))) >> 1
        result += (n2 * (5 + (n - n % 5))) >> 1
        result += (n3 * (7 + (n - n % 7))) >> 1
        result -= (n4 * (15 + (n - n % 15))) >> 1
        result -= (n5 * (21 + (n - n % 21))) >> 1
        result -= (n6 * (35 + (n - n % 35))) >> 1
        result += (n7 * (105 + (n - n % 105))) >> 1
        return result

    def sumOfMultiples1(self, n: int) -> int:
        result = 0
        for i in range(1, n + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                result += i
        return result


s = Solution()
print(s.sumOfMultiples(7))
print(s.sumOfMultiples(10))
print(s.sumOfMultiples(9))
