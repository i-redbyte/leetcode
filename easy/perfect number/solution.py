class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 2:
            return False
        p = [2, 3, 5, 7, 13, 17, 19, 31]
        for i in p:
            if self.euclid_euler(i) == num:
                return True
        return False

    def euclid_euler(self, p: int) -> int:
        return (1 << (p - 1)) * ((1 << p) - 1)

    def checkPerfectNumberSimpleVersion(self, num: int) -> bool:  # decision in the forehead
        result = 0
        if num <= 2:
            return False
        for i in range(1, (num // 2) + 1):
            if num % i == 0:
                result += i
        return result == num


s = Solution()
print(s.checkPerfectNumber(120))
print(s.checkPerfectNumber(28))
print(s.checkPerfectNumber(6))
print(s.checkPerfectNumber(496))
print(s.checkPerfectNumber(8128))
print(s.checkPerfectNumber(2))
print(s.checkPerfectNumber(3))
print(s.checkPerfectNumber(123))
print(s.checkPerfectNumber(33550336))
