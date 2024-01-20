class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        prev = "1"
        for i in range(2, n + 1):
            curr = ""
            count = 1
            for j in range(1, len(prev)):
                if prev[j] == prev[j - 1]:
                    count += 1
                else:
                    curr += str(count) + prev[j - 1]
                    count = 1
            curr += str(count) + prev[-1]
            prev = curr
        return prev


s = Solution()
print(s.countAndSay(1))
print(s.countAndSay(4))
