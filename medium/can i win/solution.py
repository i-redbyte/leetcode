class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if (maxChoosableInteger + 1) * maxChoosableInteger // 2 < desiredTotal:
            return False
        memo = {}

        def compute(num: int, current_total: int) -> bool:
            if num in memo:
                return memo[num]
            for i in range(maxChoosableInteger):
                current_bit = 1 << i
                if current_bit & num == 0:
                    if i + 1 >= current_total or not compute(num | current_bit, current_total - (i + 1)):
                        memo[num] = True
                        return True
            memo[num] = False
            return False

        return compute(0, desiredTotal)


s = Solution()
print(s.canIWin(maxChoosableInteger=10, desiredTotal=11))
print(s.canIWin(maxChoosableInteger=10, desiredTotal=0))
print(s.canIWin(maxChoosableInteger=10, desiredTotal=1))
