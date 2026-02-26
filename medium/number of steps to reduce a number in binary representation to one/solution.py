class Solution:
    def numSteps(self, s: str) -> int:
        if s == "1":
            return 0
        steps = 0
        carry = 0
        for i in range(len(s) - 1, 0, -1):
            if s[i] == '0':
                if carry == 0:
                    steps += 1  # ...0 -> /2
                else:
                    steps += 2  # ...0 + carry = ...1 -> +1, /2
            else:  # '1'
                if carry == 0:
                    steps += 2  # ...1 -> +1, /2
                    carry = 1
                else:
                    steps += 1  # ...1 + carry = ...2 (чётное) -> /2
        return steps + carry


s = Solution()
print(s.numSteps(s="1101"))
print(s.numSteps("10"))
print(s.numSteps("1"))
