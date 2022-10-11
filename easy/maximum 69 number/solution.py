class Solution:
    def maximum69Number(self, num: int) -> int:
        current = 0
        firstSixIndex = -1
        copyValue = num
        while copyValue:
            if copyValue % 10 == 6:
                firstSixIndex = current
            copyValue //= 10
            current += 1

        if firstSixIndex == -1:
            return num
        else:
            return num + 3 * (10 ** firstSixIndex)

    def maximum69Number1(self, num: int) -> int:
        s = str(num)
        n = len(s)
        for i in range(n):
            if s[i] == '6':
                return int(s[:i] + "9" + s[i + 1:])
        return int(s)


s = Solution()
print(s.maximum69Number(9669))
print(s.maximum69Number(9999))
print(s.maximum69Number(9996))
