from typing import List
from math import isqrt


class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def can_finish(t: int) -> bool:
            removed = 0

            for w in workerTimes:
                # Ищем max x: w * x * (x + 1) // 2 <= t
                # x = floor((sqrt(1 + 8*t/w) - 1) / 2)
                # Чтобы избежать float-ошибок, используем целочисленный корень:
                x = (isqrt(1 + (8 * t) // w) - 1) // 2

                # Иногда из-за //w оценка может оказаться на 1 больше допустимой,
                # поэтому аккуратно подправим.
                while w * x * (x + 1) // 2 > t:
                    x -= 1
                while w * (x + 1) * (x + 2) // 2 <= t:
                    x += 1

                removed += x
                if removed >= mountainHeight:
                    return True

            return False

        left = 0
        right = min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2

        while left < right:
            mid = (left + right) // 2
            if can_finish(mid):
                right = mid
            else:
                left = mid + 1

        return left


s = Solution()
print(s.minNumberOfSeconds(mountainHeight=4, workerTimes=[2, 1, 1]))
print(s.minNumberOfSeconds(mountainHeight=10, workerTimes=[3, 2, 2, 4]))
print(s.minNumberOfSeconds(mountainHeight=5, workerTimes=[1]))
