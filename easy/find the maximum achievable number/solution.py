class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + 2 * t


print(Solution().theMaximumAchievableX(num=4, t=1))
print(Solution().theMaximumAchievableX(3, 2))
