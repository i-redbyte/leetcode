from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        if n < 1:
            return result
        if n <= 2:
            for i in range(1, n + 1):
                result.append(str(i))
            return result
        n += 1
        for i in range(1, n):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0 and i % 5 != 0:
                result.append("Fizz")
            elif i % 3 != 0 and i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result


s = Solution()
print(s.fizzBuzz(1))
print(s.fizzBuzz(2))
print(s.fizzBuzz(3))
print(s.fizzBuzz(5))
print(s.fizzBuzz(15))
