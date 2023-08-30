class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        col = ord(coordinates[1]) - 48  # ord('0')
        row = ord(coordinates[0]) - 96  # ord('a)-1
        if (row % 2 == 0 and col % 2 != 0) or (row % 2 != 0 and col % 2 == 0):
            return True
        return False


s = Solution()
print(s.squareIsWhite("a1"))
print(s.squareIsWhite("h3"))
print(s.squareIsWhite("c7"))
print(s.squareIsWhite("g4"))
print(s.squareIsWhite("d4"))
