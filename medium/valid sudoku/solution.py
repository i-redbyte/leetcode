from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isDuplicate(nums: List[str]) -> bool:
            seen = [False] * 9
            for num in nums:
                if num != '.':
                    index = int(num) - 1
                    if seen[index]:
                        return True
                    seen[index] = True
            return False

        for row in board:
            if isDuplicate(row):
                return False
        for col in range(9):
            if isDuplicate([board[row][col] for row in range(9)]):
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if isDuplicate(box):
                    return False
        return True


s = Solution()
print(s.isValidSudoku(board=
                      [["5", "3", ".", ".", "7", ".", ".", ".", "."]
                          , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                          , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                          , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                          , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                          , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                          , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                          , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                          , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

                      ))
print(s.isValidSudoku(board=
                      [["8", "3", ".", ".", "7", ".", ".", ".", "."]
                          , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                          , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                          , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                          , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                          , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                          , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                          , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                          , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
                      ))
