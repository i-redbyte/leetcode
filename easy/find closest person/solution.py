class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        dx = abs(x - z)
        dy = abs(y - z)
        if dx == dy:
            return 0
        return 1 if dx < dy else 2


s = Solution()
print(s.findClosest(x=2, y=7, z=4))
print(s.findClosest(x=2, y=5, z=6))
print(s.findClosest(x=1, y=5, z=3))
