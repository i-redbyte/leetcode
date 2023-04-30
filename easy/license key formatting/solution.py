class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        n = len(s)
        count = 0
        result = ""
        for i in reversed(range(n)):
            if s[i] != '-':
                result += s[i].upper()
                count = count + 1
                if count == k:
                    count = 0
                    result += '-'
        m = len(result)
        if m > 0 and result[m - 1] == '-':
            result = result[:-1]
        return result[::-1]


s = Solution()
print(s.licenseKeyFormatting(s="5F3Z-2e-9-w", k=4))
print(s.licenseKeyFormatting(s="2-5g-3-J", k=2))
