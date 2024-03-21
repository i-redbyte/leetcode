from typing import List

class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        memo = {}

        def getNumberOfDigits(n: int) -> int:
            if n in memo:
                return memo[n]
            numberOfDigits = 0
            while n:
                numberOfDigits += 1
                n //= 10
            memo[n] = numberOfDigits
            return numberOfDigits

        def getCapacity(n: int, limit: int) -> int:
            numberOfDigits = getNumberOfDigits(n)
            p = 100
            chunkCount = min(9, n)
            capacity = (limit - 4 - numberOfDigits) * chunkCount
            d = 1
            while d < numberOfDigits:
                chunkCapacity = (limit - 3 - numberOfDigits - (d + 1))
                nextChunkCount = min(p - 1, n)
                capacity += chunkCapacity * (nextChunkCount - chunkCount)
                chunkCount = nextChunkCount
                p *= 10
                d += 1
            return capacity

        def split(message: str, limit: int, n: int) -> List[str]:
            capacity = limit - getNumberOfDigits(n) - 3
            result = []
            j = 0
            for i in range(1, n + 1):
                chunkCapacity = capacity - getNumberOfDigits(i)

                toWrite = min(chunkCapacity, len(message) - j)
                part = f"{message[j:j + toWrite]}<{i}/{n}>"
                j += toWrite
                result.append(part)
            return result

        len_message = len(message)
        maxDigits = (limit - 4) // 2
        maxCount = 1
        while getNumberOfDigits(maxCount) <= maxDigits and maxCount <= len(message):
            maxCount *= 10
            pos = 1
            count = maxCount - 1
            while count:
                nextCount = count // 2
                mid = pos + nextCount
                if getCapacity(mid, limit) < len_message:
                    pos = mid + 1
                    count -= nextCount + 1
                else:
                    count = nextCount
            if pos < maxCount:
                return split(message, limit, pos)
        return []


s = Solution()
print(s.splitMessage(message="this is really a very awesome message", limit=9))
print(s.splitMessage(message="short message", limit=15))
