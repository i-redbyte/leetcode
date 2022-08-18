import collections
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = collections.Counter(arr)
        sorted_counters = sorted(d.values(), reverse=True)
        n = len(arr) // 2
        result = 0
        while n > 0:
            n -= sorted_counters[result]
            result += 1
        return result

    def minSetSize1(self, arr: List[int]) -> int:
        result = 0
        s = 0
        n = len(arr) // 2
        d = collections.Counter(arr)
        print(d)
        for i, v in d.most_common():
            if v >= n or s >= n:
                if result == 0:
                    return 1
                return result
            else:
                s += v
            result += 1
        return result


print(Solution().minSetSize([3, 3, 3, 3, 5, 5, 5, 2, 2, 7]))
print(Solution().minSetSize([7, 7, 7, 7, 7, 7]))
