from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
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
