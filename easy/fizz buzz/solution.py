from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        fizzbuzz_dict = {3: "Fizz", 5: "Buzz"}
        n += 1
        for num in range(1, n):
            tmp = ""
            for key in fizzbuzz_dict.keys():
                if num % key == 0:
                    tmp += fizzbuzz_dict[key]
            if tmp == "":
                tmp = str(num)
            result.append(tmp)
        return result

    def fizzBuzz2(self, n: int) -> List[str]:
        result = []
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
print(s.fizzBuzz2(15))
print(s.fizzBuzz2(1))
print(s.fizzBuzz2(2))
print(s.fizzBuzz2(0))
