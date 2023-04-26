class Solution:
    def digitSum(self, s: str, k: int) -> str:
        if len(s) <= k:
            return s
        result = ""
        for i in range(0, len(s), ++k):
            substring = s[i:i + k]
            c = 0
            for j in substring:
                c += int(j)
            result += str(c)
        return self.digitSum(result, k)


s = Solution()
print(s.digitSum(s="11111222223", k=3))
print(s.digitSum(s="00000000", k=3))
