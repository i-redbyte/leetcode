class Solution:
    def checkValidString(self, s: str) -> bool:
        left = right = 0
        for char in s:
            if char == '(':
                left += 1
                right += 1
            elif char == ')':
                left -= 1
                right -= 1
            else:
                left -= 1
                right += 1

            if right < 0:
                break
            left = max(left, 0)

        return left == 0

s = Solution()
print(s.checkValidString("()"))
print(s.checkValidString("(*)"))
print(s.checkValidString("(*))"))
