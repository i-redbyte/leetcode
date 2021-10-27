class Solution:

    def isNumber(self, s: str) -> int:
        result = ""
        for i in s:
            if i in "1234567890":
                result += i
            else:
                return -1
        return int(result)

    def areNumbersAscending(self, s: str) -> bool:
        nums = [int(i) for i in s.split() if i.isdigit()]
        return all(i < j for i, j in zip(nums, nums[1:]))

    def areNumbersAscending1(self, s: str) -> bool:
        words = s.split()
        prev = -1
        for w in words:
            number = self.isNumber(w)
            if number != -1:
                if prev < number:
                    prev = number
                else:
                    return False
        return True


s = Solution()
print(s.areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles"))
print(s.areNumbersAscending("hello world 5 x 5"))
print(s.areNumbersAscending("sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"))
print(s.areNumbersAscending("4 5 11 26"))
