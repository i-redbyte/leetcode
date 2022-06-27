class Solution:
    def minPartitions(self, n: str) -> int:
        result = "0"
        for ch in n:
            result = max(ch, result)
        return int(result)


s = Solution()
print(s.minPartitions(n="32"))
print(s.minPartitions(n="82734"))
print(s.minPartitions(n="27346209830709182346"))
