class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        stack = []
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(ch)
            if ch == ')':
                stack.pop()
            if len(stack) == 0:
                result = s[1:i]
                result += self.removeOuterParentheses(s[i + 1:])
                break
        return result


s = Solution()
print(s.removeOuterParentheses("(()())(())"))
print(s.removeOuterParentheses("(()())(())(()(()))"))
print(s.removeOuterParentheses("()()"))
