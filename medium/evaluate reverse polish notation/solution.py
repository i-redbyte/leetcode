from typing import List
#

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = '+-*/'
        for token in tokens:
            if token in operations:
                a = int(stack.pop())
                b = int(stack.pop())
                if token == '+':
                    stack += [b + a]
                elif token == '-':
                    stack += [b - a]
                elif token == '*':
                    stack += [b * a]
                else:
                    stack += [b / a]
            else:
                stack.append(token)
        return int(stack.pop())


s = Solution()
print(s.evalRPN(["2", "1", "+", "3", "*"]))
print(s.evalRPN(["4", "13", "5", "/", "+"]))
print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
