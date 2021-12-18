from bisect import bisect
from typing import List

from urllib3.connectionpool import xrange


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        dn = len(digits)
        str_n = str(n)
        size = len(str_n)
        a = []
        for c in str_n:
            if c in digits:
                a.append(digits.index(c) + 1)
            else:
                i = bisect(digits, c)
                a.append(i)
                if i == 0:
                    for j in xrange(len(a) - 1, 0, -1):
                        if a[j]:
                            break
                        a[j] += dn
                        a[j - 1] -= 1
                a.extend([dn] * (size - len(a)))
                break
        result = 0
        for x in a:
            result = result * dn + x
        return result


s = Solution()

print(s.atMostNGivenDigitSet(["1", "3", "5", "7"], 100))
print(s.atMostNGivenDigitSet(["1", "4", "9"], 1000000000))
