from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        result, i, n = 0, 0, len(seats)
        seats.sort()
        students.sort()
        while i < n:
            result += abs(seats[i] - students[i])
            i += 1
        return result


s = Solution()
print(s.minMovesToSeat(seats=[3, 1, 5], students=[2, 7, 4]))
print(s.minMovesToSeat(seats=[4, 1, 5, 9], students=[1, 3, 2, 6]))
print(s.minMovesToSeat(seats=[2, 2, 6, 6], students=[1, 3, 2, 6]))
