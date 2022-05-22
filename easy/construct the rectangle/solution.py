import math
from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        mid = int(math.sqrt(area))
        while mid > 0:
            if not (area % mid):
                return [area // mid, mid]
            mid -= 1
        return []


s = Solution()
print(s.constructRectangle(4))
print(s.constructRectangle(37))
print(s.constructRectangle(122122))
