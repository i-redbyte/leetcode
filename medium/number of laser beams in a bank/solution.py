from typing import List


class Solution:

    def numberOfBeams(self, bank: List[str]) -> int:
        def popcount(x: int) -> int:
            c = 0
            while x:
                x &= x - 1
                c += 1
            return c

        total = 0
        prev = 0

        for row in bank:
            mask = int(row, 2)
            if mask == 0:
                continue
            cnt = popcount(mask)
            if prev:
                total += prev * cnt
            prev = cnt

        return total

    def numberOfBeams1(self, bank: List[str]) -> int:
        total = 0
        prev = 0

        for row in bank:
            cnt = row.count('1')
            if cnt == 0:
                continue
            if prev != 0:
                total += prev * cnt
            prev = cnt

        return total


s = Solution()
print(s.numberOfBeams(bank=["011001", "000000", "010100", "001000"]))
print(s.numberOfBeams(bank=["000", "111", "000"]))
