class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return arrivalTime + delayedTime if arrivalTime + delayedTime < 24 else arrivalTime + delayedTime - 24


s = Solution()
print(s.findDelayedArrivalTime(arrivalTime=15, delayedTime=5))
print(s.findDelayedArrivalTime(arrivalTime=13, delayedTime=11))
