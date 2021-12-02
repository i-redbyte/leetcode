class Solution:
    def maxDepth(self, s: str) -> int:
        counter = 0
        result = 0
        for ch in s:
            if ch == '(':
                counter += 1
            elif ch == ')':
                counter -= 1
            if counter == -1:
                return -1
            result = max(result, counter)
        return result


s = Solution()

print(s.maxDepth("(1+(2*3)+((8)/4))+1"))
print(s.maxDepth("(1)+((2))+(((3)))"))
print(s.maxDepth("(2*3)/(2-1)"))
print(s.maxDepth("1"))
