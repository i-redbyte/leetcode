class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        max_len = 0
        temp_len = 0
        for ch in s:
            if ch == '(':
                stack.append(temp_len)
                temp_len = 0
            elif ch == ')':
                if stack:
                    temp_len += stack.pop() + 2
                    max_len = max(temp_len, max_len)
                else:
                    temp_len = 0
        return max_len


s = Solution()
print(s.longestValidParentheses("(()"))
print(s.longestValidParentheses(")()())"))
print(s.longestValidParentheses(""))
