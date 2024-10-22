class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        max_count = 0
        n = len(s)

        def dfs(start, used):
            nonlocal max_count
            if start == n:
                max_count = max(max_count, len(used))
                return
            if n - start + len(used) <= max_count:
                return
            for end in range(start + 1, n + 1):
                substr = s[start:end]
                if substr not in used:
                    used.add(substr)
                    dfs(end, used)
                    used.remove(substr)

        dfs(0, set())
        return max_count


s = Solution()
print(s.maxUniqueSplit("ababccc"))
print(s.maxUniqueSplit("aba"))
print(s.maxUniqueSplit("aa"))
