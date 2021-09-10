class Solution:
    def findIntegers(self, n: int) -> int:
        arr = [0] * 32
        arr[0] = 1
        arr[1] = 2
        for i in range(2, 32):
            arr[i] = arr[i - 1] + arr[i - 2]
        i = 30
        result = 0
        bit = 0
        while i >= 0:
            if (n & (1 << i)) != 0:
                result += arr[i]
                if bit == 1:
                    result -= 1
                    break
                bit = 1
            else:
                bit = 0
            i -= 1
        return result + 1


s = Solution()
print(s.findIntegers(5))
print(s.findIntegers(1))
print(s.findIntegers(2))
print(s.findIntegers(256))
print(s.findIntegers(1024))
print(s.findIntegers(1023))
print(s.findIntegers(35768))
