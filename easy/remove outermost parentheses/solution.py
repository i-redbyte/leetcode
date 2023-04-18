class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        start = end = 0
        counter = {"(": 0, ")": 0}
        for ch in s:
            counter[ch] += 1
            end += 1
            if counter["("] == counter[")"]:
                result += s[start + 1:end - 1]
                start = end
        return result

    def removeOuterParentheses2(self, s: str) -> str:
        result = ""
        counter = 0
        for i, ch in enumerate(s):
            if ch == '(':
                counter += 1
            if ch == ')':
                counter -= 1
            if counter == 0:
                result = s[1:i]
                result += self.removeOuterParentheses(s[i + 1:])
                break
        return result

    def removeOuterParentheses1(self, s: str) -> str:
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
