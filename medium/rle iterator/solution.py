import bisect
from typing import List


class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.idx = i = 0
        self.arr = []
        self.num = []
        count = 0
        while i < len(encoding):
            e = encoding[i]
            num = encoding[i + 1]
            i += 2
            if e == 0:
                continue
            count += e
            self.arr.append(count)
            self.num.append(num)

    def next(self, n: int) -> int:
        self.idx += n
        i = bisect.bisect_left(self.arr, self.idx)
        if i < len(self.arr):
            return self.num[i]
        else:
            return -1
