class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        result = 1
        cur = 1
        for i in range(1, n):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                cur = 1
            if cur > result:
                result = cur

        def best_two(x: str, z: str) -> int:
            best = 0
            diff = 0
            first_el = {0: -1}
            for i, ch in enumerate(s):
                if ch == z:
                    diff = 0
                    first_el = {0: i}
                    continue
                diff += 1 if ch == x else -1
                if diff in first_el:
                    best = max(best, i - first_el[diff])
                else:
                    first_el[diff] = i
            return best

        result = max(result, best_two('a', 'c'))
        result = max(result, best_two('a', 'b'))
        result = max(result, best_two('b', 'a'))

        a = b = c = 0
        first = {(0, 0): 0}
        for i, ch in enumerate(s, 1):
            if ch == 'a':
                a += 1
            elif ch == 'b':
                b += 1
            else:
                c += 1
            key = (a - b, a - c)
            if key in first:
                result = max(result, i - first[key])
            else:
                first[key] = i

        return result


s = Solution()
print(s.longestBalanced("abbac"))
print(s.longestBalanced("aabcc"))
print(s.longestBalanced("aba"))
