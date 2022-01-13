class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        guides = ((0, 1), (1, 0), (0, -1), (-1, 0))
        pos = (0, 0)
        head = 0
        for symbol in instructions:
            if symbol == "L":
                head = (head - 1) % 4
            elif symbol == "R":
                head = (head + 1) % 4
            else: #G
                pos = (pos[0] + guides[head][0], pos[1] + guides[head][1])
        return pos == (0, 0) or head != 0


s = Solution()
print(s.isRobotBounded("GGLLGG"))
print(s.isRobotBounded("GG"))
print(s.isRobotBounded("GL"))
