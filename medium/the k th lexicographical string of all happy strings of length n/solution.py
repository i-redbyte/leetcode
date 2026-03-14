class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total = 3 * (1 << (n - 1))
        if k > total:
            return ""

        chars = ['a', 'b', 'c']
        result = []

        prev = ''
        for pos in range(n):
            block = 1 << (n - pos - 1)

            for ch in chars:
                if ch == prev:
                    continue

                if k > block:
                    k -= block
                else:
                    result.append(ch)
                    prev = ch
                    break

        return ''.join(result)


s = Solution()
print(s.getHappyString(n=1, k=3))
print(s.getHappyString(n=1, k=4))
print(s.getHappyString(n=3, k=9))
