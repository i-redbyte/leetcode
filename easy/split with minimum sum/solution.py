class Solution:
    def splitNum(self, num: int) -> int:
        arr = [int(x) for x in str(num)]
        arr.sort()
        num1 = 0
        num2 = 0
        for i in range(0, len(arr)):
            if i % 2 == 0:
                num1 = num1 * 10 + arr[i]
            elif i % 2 != 0:
                num2 = num2 * 10 + arr[i]
        return num1 + num2

    def splitNum1(self, num: int) -> int:
        s = sorted(str(num))
        return int("".join(s[::2])) + int("".join(s[1::2]))


s = Solution()
print(s.splitNum(4325))
print(s.splitNum(687))
