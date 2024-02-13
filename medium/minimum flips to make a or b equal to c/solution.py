class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        for i in range(32):
            bit_a = (a >> i) & 1
            bit_b = (b >> i) & 1
            bit_c = (c >> i) & 1
            if bit_a | bit_b != bit_c:
                if bit_c == 1:
                    flips += 1
                else:
                    flips += bit_a + bit_b
        return flips


s = Solution()
print(s.minFlips(a=2, b=6, c=5))
print(s.minFlips(a=4, b=2, c=7))
print(s.minFlips(a=1, b=2, c=3))
