from typing import List


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        n1, n2 = len(num1), len(num2)
        res: List[int] = [0] * (n1 + n2)

        for i in reversed(range(n1)):
            for j in reversed(range(n2)):
                z: int = int(num1[i]) * int(num2[j])
                d = (z + res[i + j + 1]) // 10
                m = (z + res[i + j + 1]) % 10
                res[i + j + 1] = m
                res[i + j] += d

        z: str = "".join(map(str, res))
        return z[1:] if z[0] == "0" else z


s = Solution()
print(s.multiply("2", "2"))
print(s.multiply("123", "456"))
print(s.multiply("10", "56"))
print(s.multiply("11", "11"))
print(s.multiply("111", "1111"))
print(s.multiply("11111111111111", "1111111111111"))
