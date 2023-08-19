class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return ''.join(sorted(s))
        result = s
        n = len(s)
        for i in range(1, n):
            result = min(result, s[i:] + s[:i])
        return result


s = Solution()
print(s.orderlyQueue(s="cba", k=1))
print(s.orderlyQueue(s="baaca", k=3))
