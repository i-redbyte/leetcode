from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0])
        location = []
        for start_column in range(n):
            location.append(self.find_ball_location(grid, start_column))
        return location

    def find_ball_location(self, grid: List[List[int]], start: int) -> int:
        count_rows = len(grid)
        count_columns = len(grid[0])
        column_location = start
        for row_location in range(count_rows):
            if grid[row_location][column_location] == 1 and column_location + 1 < count_columns and \
                    grid[row_location][column_location + 1] == 1:
                column_location = column_location + 1
                continue
            if grid[row_location][column_location] == -1 and column_location - 1 >= 0 and \
                    grid[row_location][column_location - 1] == -1:
                column_location = column_location - 1
                continue
            return -1
        return column_location


s = Solution()

print(s.findBall([[1, 1, 1, -1, -1], [1, 1, 1, -1, -1], [-1, -1, -1, 1, 1], [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]]))
print(s.findBall([[-1]]))
print(s.findBall([[1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1], [1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1]]))
