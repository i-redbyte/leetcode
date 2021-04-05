class Solution:
    def isValid(self, s: str) -> bool:
        close_parent = {"(": ")", "[": "]", "{": "}"}
        open_parent = {"(", "[", "{"}
        parent_stack = []
        for current_char in s:
            if current_char in open_parent:
                parent_stack.append(current_char)
            elif parent_stack and current_char == close_parent[parent_stack[-1]]:
                parent_stack.pop()
            else:
                return False
        return parent_stack == []


s = Solution()
print(s.isValid("()"))
print(s.isValid(")(()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))
print(s.isValid("([)]"))
print(s.isValid("{[]}"))
print(s.isValid("(("))
