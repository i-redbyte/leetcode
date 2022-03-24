from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people) - 1
        people.sort()
        i = 0
        result = 0
        while i <= n:
            result += 1
            if people[i] + people[n] <= limit:
                i += 1
            n -= 1
        return result


s = Solution()
print(s.numRescueBoats(people=[1, 2], limit=3))
print(s.numRescueBoats(people=[3, 2, 2, 1], limit=3))
print(s.numRescueBoats([3, 5, 3, 4], limit=5))
