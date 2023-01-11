from typing import List


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        Kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.80 + 32.00
        return [Kelvin, Fahrenheit]


s = Solution()
print(s.convertTemperature(36.50))
print(s.convertTemperature(122.11))
