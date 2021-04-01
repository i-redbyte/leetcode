class Solution:
    def reverseBits(self, str) -> str:
        n = self.binary_to_dec(str)
        result = 0
        power_two = 31
        while n != 0:
            result += (n & 1) << power_two
            n = n >> 1
            power_two -= 1
        return "{} ({:032b})".format(result, result)

    def binary_to_dec(self, s: str) -> int:
        s = reversed(s)
        power_two = 0
        result = 0
        for i in s:
            result += pow(2, power_two) * int(i)
            power_two += 1
        return result


s = Solution()
print(s.reverseBits("00000010100101000001111010011100"))
print(s.reverseBits("11111111111111111111111111111101"))
print(s.reverseBits("00000000000000000000000000000000"))
print(s.reverseBits("10100000000000000000000000000001"))
print(s.reverseBits("11100000000000000000000000000000"))
