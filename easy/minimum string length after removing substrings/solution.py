class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for char in s:
            if stack and ((stack[-1] == 'A' and char == 'B') or (stack[-1] == 'C' and char == 'D')):
                stack.pop()
            else:
                stack.append(char)
        return len(stack)


s = Solution()
print(s.minLength("ABFCACDB"))
print(s.minLength("ACBBD"))
