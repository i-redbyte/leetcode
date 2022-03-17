class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                val = stack.pop()
                stack[-1] += max(2 * val, 1)
        return stack.pop()


s = Solution()
print(s.scoreOfParentheses("()"))
print(s.scoreOfParentheses("(())"))
print(s.scoreOfParentheses("()()"))
print(s.scoreOfParentheses("(()(()))"))
