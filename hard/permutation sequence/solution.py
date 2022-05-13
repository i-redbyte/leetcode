class Solution:
    def fak(self, n: int) -> int:
        if n == 0:
            return 1
        return n * self.fak(n - 1)

    def getPermutation(self, n: int, k: int) -> str:
        factor = self.fak(n)
        num = []
        for i in range(1, n + 1):
            num.append(str(i))
        result = ''
        for i in range(n, 1, -1):
            factor = int(factor / i)
            (bucket, k) = divmod(k, factor)
            if k == 0:
                bucket -= 1
            result += num[bucket]
            del num[bucket]
        return result + num[0]


s = Solution()
print(s.getPermutation(n=3, k=3))
print(s.getPermutation(n=4, k=9))
print(s.getPermutation(n=3, k=1))
