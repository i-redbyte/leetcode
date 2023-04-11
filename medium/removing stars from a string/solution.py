class Solution:
    def removeStars(self, s: str) -> str:
        result = ""
        i = 0
        n = len(s)
        while i < n:
            if s[i] == '*':
                result = result[:-1]
            else:
                result += s[i]
            i += 1
        return result

    def removeStars2(self, s: str) -> str:
        stack = []
        result = ""
        for ch in s:
            if len(stack) > 0 and ch == '*':
                stack.pop()
            else:
                stack.append(ch)
        if len(stack) == 0:
            return result
        while stack:
            result = stack[-1] + result
            stack.pop()
        return result

    def removeStars1(self, s: str) -> str:
        characters = [""] * len(s)
        result = ""
        k = 0
        for ch in s:
            if ch == '*':
                k -= 1
            else:
                characters[k] = ch
                k += 1
        for i in range(k):
            result += characters[i]
        return result


s = Solution()
print(s.removeStars("leet**cod*e"))
print(s.removeStars("erase*****"))
print(s.removeStars("asfdsf"))
print(s.removeStars("abb*cdfg*****x*"))
