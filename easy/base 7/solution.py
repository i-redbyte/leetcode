class Solution:
    def convertToBase7(self, num: int) -> str:
        if num < 0:
            return '-' + str(self.convertToBase7(abs(num)))
        else:
            if num < 7:
                return str(num)
            else:
                return str(self.convertToBase7(num // 7)) + str(num % 7)


s = Solution()
print(s.convertToBase7(100))
print(s.convertToBase7(-7))
